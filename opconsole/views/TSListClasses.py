import datetime
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


def getDctNodeSkel(userfullName):
    return {"fullname": userfullName,"total": 0,
        "months": {x: {'inserted': 0,'time': 0,'temp_time': 0, "free":0, "temp_free":0} for x in range(1, 13)}}


def computeAnnualHours(qrySet):
    timeStampWithDuration = {}
    free=False
    for timestamp in qrySet:

        tmps = QrySetTimestamp(timestamp)

        if  tmps.getUserId() not in timeStampWithDuration.keys():
            timeStampWithDuration[tmps.getUserId()] = getDctNodeSkel(tmps.getFullName())

        insertCount = timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"]
        if insertCount % 2 != 0:
            e_time = tmps.getTimeInSeconds() - timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_time"]
            timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["time"] += e_time
            timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_free"] = tmps.getTimeInSeconds()
        else:
            if insertCount > 0:
                diffTime =  tmps.getTimeInSeconds() - timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_free"]
                timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["free"] += diffTime

            timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["temp_time"] = tmps.getTimeInSeconds()


        timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"] = timeStampWithDuration[tmps.getUserId()]["months"][tmps.getMonth()]["inserted"] + 1

    for user in timeStampWithDuration:
        for month in timeStampWithDuration[user]["months"]:
            timeStampWithDuration[user]["total"] += timeStampWithDuration[user]["months"][month]["time"]
    return timeStampWithDuration

