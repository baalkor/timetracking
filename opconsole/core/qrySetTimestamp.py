import datetime
class QrySetTimestamp(object):
    year = 0
    month = 0
    day = 0
    currUserId = ""
    currScope =  0
    userfullName = ""
    tOb = None

    def getYear(self): return self.year

    def getDay(self): return self.day

    def getMonth(self): return self.month

    def parseFullName(self, timestamps): return "%s, %s" % (timestamps["user__user__last_name"], timestamps["user__user__first_name"])

    def getDateStr(self, timestamps): return "%d-%d-%d %d:%d:%d" % ( timestamps["year"], timestamps["month"], timestamps["day"], timestamps["hours"], timestamps["minutes"], timestamps["seconds"])

    def getTime(self, timestamps): return datetime.datetime.strptime(self.getDateStr(timestamps), "%Y-%m-%d %H:%M:%S")

    def getUserId(self): return self.currUserId

    def getScopeVal(self ): return self.currScope

    def getFullName(self):return self.userfullName

    def getTimestampObj(self):return self.tOb

    def getTimeInSeconds(self):return self.getTimeDelta(self.getTimestampObj()).total_seconds()

    def getTimeDelta(self, date): return (date - datetime.datetime(1970, 1, 1))


    def parseScope(self, scope):

        scope = scope.lower()
        if scope == "months":
            scope="month"
        elif scope == "weeks":
            scope = "week"
        elif scope == "days":
            scope = "days"
        else:
            raise RuntimeError("Invalid scope %s" % scope)
        return scope



    def __init__(self, timestamps, scope="months"):

        scope = self.parseScope(scope)
        self.currUserId = timestamps["user__id"]
        self.currScope = timestamps["month"]
        self.userfullName = self.parseFullName(timestamps)
        self.tOb = self.getTime(timestamps)
        self.year = timestamps["year"]
        self.month = timestamps["month"]
        self.day = timestamps["day"]


