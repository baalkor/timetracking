from django.views.generic import ListView, DetailView
from django.http.response import HttpResponseForbidden
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.db.models import DateTimeField, F,  Min, Max, Count, DurationField, ExpressionWrapper
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractMinute, ExtractHour, ExtractSecond
from opconsole.models import Timesheets, Employes, Device
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.conf import settings
from datetime import datetime, timedelta
import calendar
from time import mktime as mktime

from django.db.models import Q,F, Sum ,IntegerField
from django.db.models.functions import TruncHour, TruncMinute, TruncSecond

import datetime

class TestIsMyTimestampOrStaff(UserPassesTestMixin):
    def test_func(self, request, timeid):
        return self.request.user.is_staff() or \
            Timesheets.object.get(pk=timeid).user.user == self.request.user


def get_date_or_now(request):
    try:
        date = datetime.datetime.strptime(request.GET.get('date'), "%Y-%m-%d")
    except ( ValueError , TypeError ):
        date = datetime.datetime.now()
    finally:
        return date

def get_employee_or_request(request):
    try:

        uid = int(request.GET.get('userId'))

        isContentAdmin = request.user.groups.filter(name=settings.ADMIN_GROUP).exists()
        myId = uid == request.user

        isNotAllowedCheckingAnotherUserTMS = not myId and not isContentAdmin

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

    def get_queryset(self):
        date = get_date_or_now(self.request)

        qrySet = Timesheets.objects.filter(
            time__year=date.year
        ).values(

            "user__id",
            "user__user__first_name",
            "user__user__last_name",
        ).annotate(month=ExtractMonth("time"))

        timeStampWithDuration = []
        for timestamp in qrySet:

            print qrySet


            timeStampWithDuration.append(
                {
                    "user__id":timestamp["user__id"],
                    "user__user__first_name":timestamp["user__user__last_name"],
                    "user__user__last_name":timestamp["user__user__first_name"],
                    "month":timestamp["month"],
                    "time":timestamp["time"]
                }
            )

        print qrySet.query
        return timeStampWithDuration