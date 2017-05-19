from qrySetTimestamp import QrySetTimestamp
from timestampCount import TimestampCount
import calendar


import operator



class TimeStampsManager(object):
    timestampsDailyCount = None
    timestamps = {}
    year = 0

    def __init__(self, queryset, year):
        self.year = year
        for entry in queryset:
            parsedEntry = QrySetTimestamp(entry)

            if parsedEntry.getUserId() not in self.timestamps.keys():
                self.timestamps[parsedEntry.getUserId()] = TimestampCount(parsedEntry)
            self.timestamps[parsedEntry.getUserId()].add(parsedEntry)

    def getDailyView(self, day, month):
        found = False
        cpt = 0
        val = {}
        keys = self.timestamps.keys()

        while not found and cpt < len(self.timestamps.keys()):
            k = keys[cpt]
            found =  self.timestamps[k].getMonth() == month and self.timestamps[k].getYear() == self.year and self.timestamps[k].getDay() == day
            if not found:
                cpt=cpt+1
            else:
                val[k] = ( self.timestamps[k].count(), self.timestamps[k].get_free_time() )
        return  val


    def getMonthly(self, month):
        days = {}
        for day in range(calendar.monthrange(self.year, month)[1]):
            d = self.getDailyView(day,month)
            for key in  d:
                if key not in days : days[key] = (0,0)
                days[key] = list(days[key])
                days[key][0] += d[key][0]
                days[key][1] += d[key][1]
                days[key] = tuple(days[key])
        return days

    def getAnnualy(self):
        months = {}
        for month in range(1,13):
           m = self.getMonthly(month)
           for k in  m:
               if k not in months.keys() : months[k] = (0,0)
               months[k] = list(months[k])
               months[k][0] += m[k][0]
               months[k][1] += m[k][1]
               months[k] = tuple(months[k])

        return months



