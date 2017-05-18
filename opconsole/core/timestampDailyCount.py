class TimestampDailyCount(object):
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
    def free_time(self): return self.free

    def getDay(self): return self.day

    def getMonth(self): return self.month

    def getYear(self): return self.year

    def isEvenCount(self): return self.inserted % 2

    def add(self, QrySetTimestampObj):
        if not self.isEvenCount():
            e_time = QrySetTimestampObj.getTimeInSeconds() - self._temp_time
            self.time += e_time
            self.temp_free = QrySetTimestampObj.getTimeInSeconds()
        else:
            if self.count() > 0:
                diffTime = QrySetTimestampObj.getTimeInSeconds() - self._temp_free
                self.free += diffTime

            self._temp_time = QrySetTimestampObj.getTimeInSeconds()


        self.inserted = self.inserted+1