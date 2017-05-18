import datetime
class QrySetTimestamp(object):

    currUserId = ""
    currScope =  0
    userfullName = ""
    tOb = None

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





def genScopeDict(userfullName, scope="months"):
    return {"fullname": userfullName,"total": 0,scope: {x: {'inserted': 0,'time': 0,'temp_time': 0, "free":0, "temp_free":0} for x in range(1, 13)}}

def computeHours(qrySet, scope="months"):
    timeStampWithDuration = {}
    for timestamp in qrySet:

        tmps = QrySetTimestamp(timestamp, scope)

        if  tmps.getUserId() not in timeStampWithDuration.keys(): timeStampWithDuration[tmps.getUserId()] = genScopeDict(tmps.getFullName())

        insertCount = timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["inserted"]
        if insertCount % 2 != 0:
            e_time = tmps.getTimeInSeconds() - timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["temp_time"]
            timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["time"] += e_time
            timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["temp_free"] = tmps.getTimeInSeconds()
        else:
            if insertCount > 0:
                diffTime =  tmps.getTimeInSeconds() - timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["temp_free"]
                timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["free"] += diffTime

            timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["temp_time"] = tmps.getTimeInSeconds()


        timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["inserted"] = timeStampWithDuration[tmps.getUserId()][scope][tmps.getScopeVal()]["inserted"] + 1

    for user in timeStampWithDuration:
        for entry in timeStampWithDuration[user][scope]:
            timeStampWithDuration[user]["total"] += timeStampWithDuration[user][scope][entry]["time"]

    return timeStampWithDuration

