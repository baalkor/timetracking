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
