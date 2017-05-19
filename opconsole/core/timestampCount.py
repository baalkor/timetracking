from opconsole.templatetags.duration import duration
import datetime
class TimestampCount(object):
    time = 0.
    free = 0.
    inserted = 0
    year = 0
    month = 0
    day = 0
    userid = -1
    userfullname = ""

    _temp_time = 0.
    _temp_free = 0.

    def __init__(self, QrySetTimestampObj):

        self.userid       = QrySetTimestampObj.getUserId()
        self.userfullName = QrySetTimestampObj.getFullName()
        self.month        = QrySetTimestampObj.getMonth()
        self.year         = QrySetTimestampObj.getYear()
        self.day          = QrySetTimestampObj.getDay()
        self._temp_free   = 0.
        self._temp_time   = 0.
        self.time         = 0.
        self.free         = 0.

    def length(self) : return self.inserted

    def count(self): return self.time

    def get_free_time(self): return self.free

    def getDay(self): return self.day

    def getMonth(self): return self.month

    def getYear(self): return self.year

    def isOddCount(self): return self.inserted % 2 != 0

    def add(self, tmp):

        tmpS = tmp.getTimeInSeconds()

        if self.isOddCount() and self.inserted > 0:
            self.time +=   tmpS - self._temp_time
            self._temp_free = tmpS
        else:
            if self.inserted > 0: self.free += tmpS - self._temp_free
            self._temp_time = tmpS
        self.inserted = self.inserted+1