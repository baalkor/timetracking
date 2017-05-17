from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.db.models import DateTimeField, Min, Max
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay, ExtractMinute, ExtractHour, ExtractSecond
from opconsole.models import Timesheets, Employes, Device
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.conf import settings
from datetime import datetime, timedelta
from django.db.models import Q,F, Sum ,IntegerField
from django.db.models.functions import  TruncSecond
from django.db.models import Aggregate
import datetime
import calendar


class TestIsMyTimestampOrStaff(UserPassesTestMixin):
    def test_func(self, request, timeid):
        return self.request.user.is_staff() or \
            Timesheets.object.get(pk=timeid).user.user == self.request.user

class TimeDelta(Aggregate):
    function = ""

def get_date_or_now(request):
    try:
        date = datetime.datetime.strptime(request.GET.get('date'), "%Y-%m-%d")
    except ( ValueError , TypeError ):
        date = datetime.datetime.now()
    finally:
        return date
def isContentAdmin(request):return request.user.groups.filter(name=settings.ADMIN_GROUP).exists()

def get_employee_or_request(request):
    try:

        uid = int(request.GET.get('userId'))


        myId = uid == request.user

        isNotAllowedCheckingAnotherUserTMS = not myId and not isContentAdmin(request)

        if uid == None or isNotAllowedCheckingAnotherUserTMS:
            emp = get_object_or_404(Employes, user=request.user)
        else:
            emp = get_object_or_404(Employes, pk=uid)
        return emp
    except (TypeError, ValueError):
        return get_object_or_404(Employes, user=request.user)


@method_decorator(login_required, name='dispatch')
class TimesheetView(ListView):
    context_object_name = 'timestamps'
    template_name = "opconsole_my_timesheet.html"
    model = Timesheets
    errors = None

    def getEmployee(self):
        return get_employee_or_request(self.request)

    def computeHoursDaily(self, percentage, employee,):
        date = self.getDate()
        querySet = Timesheets.objects.distinct().annotate(
            seconds=TruncSecond("time", output_field=DateTimeField())
        ).filter(
            status='0',
            user=employee,
            recptTime__year=date.year,
            recptTime__month=date.month,
            recptTime__day=date.day
        ).order_by("time").values("seconds")

        cpt=0

        s_time = None
        e_time = None
        hoursAtWork=timedelta()
        pauseBreak=timedelta()
        freeTime = False
        for i in querySet:

            if cpt % 2 == 0:
                s_time = i["seconds"]
            else:
                tdelta = i["seconds"] - s_time
                if not freeTime:
                    print hoursAtWork
                    hoursAtWork += tdelta
                    freeTime = True
                else:
                    pauseBreak += tdelta
                    freeTime = False

            cpt = cpt + 1


        if cpt % 2 != 0: self.errors = "Odd number of valid timestamps!"

        return ( hoursAtWork, pauseBreak )

    def get_context_data(self, **kwargs):
        employee = self.getEmployee()
        hasWebDevice = Device.objects.filter(owner=employee).filter(devType='1').exists()
        context = super(TimesheetView, self).get_context_data(**kwargs)

        context["totalHours"] = self.computeHoursDaily(100,employee)
        context["hasWebDevice"] = hasWebDevice
        context["currentDate"] = self.getDate()
        context["errors"] = self.errors
        context["employeeId"] = employee.id
        context["fullname"] = "%s, %s" % ( employee.user.last_name,employee.user.first_name )
        return context

    def getDate(self):
        return get_date_or_now(self.request)


    def get_queryset(self):
        employee = self.getEmployee()
        date = self.getDate()
        return Timesheets.objects.filter(user=employee).filter(
            recptTime__year=date.year,
            recptTime__day=date.day,
            recptTime__month=date.month
        ).order_by("time")



@method_decorator(login_required, name='dispatch')
class ManualTimesheetList(ListView):
    template_name = "opconsole_manual_request.html"
    model = Timesheets


    def get_queryset(self):
        return Timesheets.objects.filter(Q(deletion=True) | Q( status='6'))



@method_decorator(login_required, name='dispatch')
class TimestampDetail(DetailView):
    model = Timesheets
    template_name = "opconsole_timestamp.html"

    def get_context_data(self, **kwargs):
        context = super(TimestampDetail, self).get_context_data(**kwargs)
        context["google_api_key"] = settings.GOOGLE_API_KEY
        return context

class QrySetTimestamp(object):

    currUserId = ""
    currMonth =  0
    userfullName = ""
    tOb = None

    def __init__(self, timestamps):
        self.currUserId = timestamps["user__id"],
        self.currMonth = timestamps["month"]
        self.userfullName = "%s, %s" % (timestamps["user__user__last_name"], timestamps["user__user__first_name"])
        timeStr = "%d-%d-%d %d:%d:%d" % ( timestamps["year"], timestamps["month"], timestamps["day"], timestamps["hours"], timestamps["minutes"], timestamps["seconds"])
        self.tOb = datetime.datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S")

    def getUserId(self): return self.currUserId

    def getMonth(self):return self.currMonth

    def getFullName(self):return self.userfullName

    def getTimestampObj(self):
        return self.tOb

    def getTimeInSeconds(self):
        return self.getTimeDelta(self.getTimestampObj()).total_seconds()

    def getTimeDelta(self, date):
        return (date - datetime.datetime(1970, 1, 1))


class TimesheetList(ListView):
    template_name = "opconsole_timesheet_list.html"
    model = Timesheets
    context_object_name = "timesheets"

    def get_context_data(self, **kwargs):
        context = super(TimesheetList, self).get_context_data(**kwargs)
        context["months"] = [ calendar.month_name[x] for x in range(1,13)]
        context["month_num"] = [ x for x in range(1,13)]
        values = Timesheets.objects.distinct().annotate(
            year=ExtractYear("time")
        ).aggregate(
            Min("time"),
            Max("time")
        )

        ymin = values["time__min"].year
        ymax = values["time__max"].year

        context["years"] = range(ymin  , ymax + 1)
        return context

    def getFilterIfContentAdmin(self):
        return Q() if isContentAdmin(self.request) else Q(user=get_employee_or_request(self.request))

    @staticmethod
    def getDctNodeSkel(userfullName):
        return {"fullname": userfullName,"total": 0,
            "months": {x: {'inserted': 0,'time': 0,'temp_time': 0} for x in range(1, 13)}}


    @staticmethod
    def computeAnnualHours(qrySet):
        timeStampWithDuration = {}

        for timestamp in qrySet:

            tmps = QrySetTimestamp(timestamp)
            if  tmps.getUserId() not in timeStampWithDuration.keys():
                timeStampWithDuration[tmps.getUserId()] = TimesheetList.getDctNodeSkel(tmps.getFullName())

            insertCount = timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"]
            if insertCount % 2 != 0 and insertCount > 0:
                e_time = tmps.getTimeInSeconds() - timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_time"]
                timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["time"] += e_time
                timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_time"] = 0
            else:
                timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_time"] =  tmps.getTimeInSeconds()

            timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"] = timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"] + 1

        TimesheetList.setTotal(timeStampWithDuration)
        return timeStampWithDuration

    def get_queryset(self):
        date = get_date_or_now(self.request)
        qrySet = Timesheets.objects.filter(
            time__year=date.year,status='0'
        ).values(
            "user__id",
            "user__user__first_name",
            "user__user__last_name"
        ).annotate(
            year=ExtractYear("time", output_field=IntegerField()),
            month=ExtractMonth("time", output_field=IntegerField()),

        ).annotate(
            day=ExtractDay("time", output_field=IntegerField()),
            seconds=ExtractSecond("time", output_field=IntegerField()),
            minutes=ExtractMinute("time", output_field=IntegerField()),
            hours=ExtractHour("time", output_field=IntegerField())
        ).filter(self.getFilterIfContentAdmin()).order_by("hours", "minutes", "seconds")

        return TimesheetList.computeAnnualHours(qrySet)

    @staticmethod
    def setTotal(tsDict):
        for user in tsDict:
            for month in tsDict[user]["months"]:
                tsDict[user]["total"] += tsDict[user]["months"][month]["time"]