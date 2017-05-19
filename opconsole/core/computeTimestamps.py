from timestampsManager import TimeStampsManager
from opconsole.templatetags import duration


def computeHours(qrySet, scope="months"):
    Mng =  TimeStampsManager(qrySet,2017)
    a = Mng.getDailyView(16,5)
    for userid in  a:
        print userid
        print duration.duration(a[userid][0])
        print duration.duration(a[userid][1])
    return ""

