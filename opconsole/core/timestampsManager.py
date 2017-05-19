from qrySetTimestamp import QrySetTimestamp
from opconsole.models import Employes
from django.shortcuts import get_object_or_404
from timestampCount import TimestampCount
import calendar

class TimestampDisplayEntry(object):
    full_name = ""
    pause_hours = 0
    working_hours = 0

    def __init__(self, user_id, data):
        user = get_object_or_404(Employes, pk=user_id)
        self.full_name = "%s, %s" % ( user.user.first_name, user.user.last_name )
        self.working_hours = data[user_id][0]
        self.pause_hours = data[user_id][1]

    def toDict(self):
        return { "full_name" : self.full_name, "working_hours":self.working_hours, "pause_hours":self.pause_hours }

class TimestampDisplay(object):
    timeStampsManager = None
    def __init__(self, timeStampsManager):
        self.timeStampsManager = timeStampsManager
    def get_full_name(self, user_id):
        user = get_object_or_404(Employes, pk=user_id)
        return "%s, %s" % (user.user.first_name, user.user.last_name)


    def sortMonthly(self, month):
        tmps = []
        for userid in self.timeStampsManager.getUserIds():
            tmps.append({
                "id": userid,
                "full_name": self.get_full_name(userid),
                "total": self.timeStampsManager.getMonthly(userid)[userid][0],
                "range": []
            })

            for r in range(1,calendar.monthrange(self.timeStampsManager.year, month)[1]):
                value = self.timeStampsManager.getDailyView(month, r, userid)
                if userid in value:
                    tmps[-1]["range"].append(value[userid][0])
                else:
                    tmps[-1]["range"].append(0)
        return tmps

    def sortAnnualy(self):
        tmps = []
        for userid in self.timeStampsManager.getUserIds():
            tmps.append({
                "id": userid,
                "full_name": self.get_full_name(userid),
                "total": self.timeStampsManager.getAnnualy(userid)[userid][0],
                "range": []
            })

            for r in range(1, 13):
                value = self.timeStampsManager.getMonthly(r, userid)
                if userid in value:
                    tmps[-1]["range"].append(value[userid][0])
                else:
                    tmps[-1]["range"].append(0)
        return tmps

    def getScopedView(self, scope, month, day):


        if scope == "annualy":
            return self.sortAnnualy()

        elif scope == "monthly":
            data = self.paddTable(self.timeStampsManager.getMonthly(month))
        elif scope == "daily":
            data = self.timeStampsManager.getDailyView(day,month)
        else:
            raise RuntimeError("Invalid scope %s" % scope)





class TimeStampsManager(object):
    timestampsDailyCount = None
    timestamps = {}
    year = 0


    def __init__(self, queryset, year):
        self.timestamps = {}
        self.year = year
        self.userIds = []
        for entry in queryset:
            parsedEntry = QrySetTimestamp(entry)

            if parsedEntry.getUserId() not in self.timestamps.keys():
                self.timestamps[parsedEntry.getUserId()] = TimestampCount(parsedEntry)


            self.timestamps[parsedEntry.getUserId()].add(parsedEntry)

    def getUserIds(self): return self.timestamps.keys()


    def getDailyView(self, day, month, userid=-1):
        found = False
        cpt = 0
        val = {}
        keys = self.timestamps.keys()

        while not found and cpt < len(self.timestamps.keys()):
            k = keys[cpt]
            found =  self.timestamps[k].getMonth() == month and self.timestamps[k].getYear() == self.year and self.timestamps[k].getDay() == day

            if userid > -1: found = found and k == userid

            if not found:
                cpt=cpt+1
            else:
                val[k] = ( self.timestamps[k].count(), self.timestamps[k].get_free_time() )
        return val


    def getMonthly(self, month, userid=-1):
        days = {}
        for day in range(calendar.monthrange(self.year, month)[1]):
            d = self.getDailyView(day,month, userid)
            for key in  d:
                if key not in days : days[key] = (0,0)
                days[key] = list(days[key])
                days[key][0] += d[key][0]
                days[key][1] += d[key][1]
                days[key] = tuple(days[key])
        return days

    def getAnnualy(self, userid = -1 ):
        months = {}
        for month in range(1,13):
           m = self.getMonthly(month, userid)
           for k in  m:
               if k not in months.keys() : months[k] = (0,0)
               months[k] = list(months[k])
               months[k][0] += m[k][0]
               months[k][1] += m[k][1]
               months[k] = tuple(months[k])

        return months




