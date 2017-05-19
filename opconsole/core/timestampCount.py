from opconsole.templatetags.duration import duration
class TimestampCount(object):
    time = 0
    free = 0
    inserted = 0
    year = 0
    month = 0
    day = 0
    userid = -1
    userfullname = ""

    _temp_time = 0
    _temp_free = 0

    def __init__(self, QrySetTimestampObj):

        self.userid       = QrySetTimestampObj.getUserId()
        self.userfullName = QrySetTimestampObj.getFullName()
        self.month        = QrySetTimestampObj.getMonth()
        self.year         = QrySetTimestampObj.getYear()
        self.day          = QrySetTimestampObj.getDay()

    def length(self) : return self.inserted

    def count(self):
        if self.isEvenCount():
            return self.time
        else:
            return 0
    def get_free_time(self): return self.free

    def getDay(self): return self.day

    def getMonth(self): return self.month

    def getYear(self): return self.year

    def isEvenCount(self): return self.inserted % 2

    def add(self, tmp):

        if tmp.getUserId() != self.userid: raise RuntimeError("Invalid userid")
        tmpS = tmp.getTimeInSeconds()
        if not self.isEvenCount() and self.inserted > 0:
            e_time = tmpS - self._temp_time
        else:
            if self.inserted > 0:
                diffTime = tmpS - self._temp_free
                self.free += diffTime
            self._temp_time = tmpS
        self.inserted = self.inserted+1