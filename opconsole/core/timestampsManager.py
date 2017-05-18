from qrySetTimestamp import QrySetTimestamp
from timestampDailyCount import TimestampDailyCount

class TimeStampsManager(object):
    timestampsDailyCount = None
    def __init__(self, queryset):
        for entry in queryset:
            raw_timestamp = QrySetTimestamp(entry)