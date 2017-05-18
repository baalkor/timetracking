from timestampDailyCount import TimestampDailyCount
from qrySetTimestamp import  QrySetTimestamp
def computeHours(qrySet, scope="months"):
    timeStampWithDuration = {}
    for timestamp in qrySet:

        tmps = QrySetTimestamp(timestamp, scope)

        if  tmps.getUserId() not in timeStampWithDuration.keys():
            timeStampWithDuration[tmps.getUserId()] = TimestampDailyCount(tmps)
        timeStampWithDuration[tmps.getUserId()].add(tmps)

    #for user in timeStampWithDuration:
    #    timeStampWithDuration[user]["total"] += timeStampWithDuration[user].count()

    return timeStampWithDuration

