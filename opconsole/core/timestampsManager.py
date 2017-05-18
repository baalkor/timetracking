from qrySetTimestamp import QrySetTimestamp
from timestampDailyCount import TimestampDailyCount
from opconsole.models import Timesheets
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay, ExtractMinute, ExtractHour, ExtractSecond
from django.db.models import Q, IntegerField
from opconsole.views.utils import get_date_or_now
class TimeStampsManager(object):
    timestampsDailyCount = None

    def getQuerySet(self):
        return Timesheets.objects.filter(
            time__year=get_date_or_now(self.request).year, status='0'
        ).values(
            "user__id",
            "user__user__first_name",
            "user__user__last_name"
        ).annotate(
            year=ExtractYear("time", output_field=IntegerField()),
            month=ExtractMonth("time", output_field=IntegerField()),
            day=ExtractDay("time", output_field=IntegerField())
        ).annotate(
            seconds=ExtractSecond("time", output_field=IntegerField()),
            minutes=ExtractMinute("time", output_field=IntegerField()),
            hours=ExtractHour("time", output_field=IntegerField())
        ).filter(self.getFilterIfContentAdmin()).order_by("hours", "minutes", "seconds")

    def __init__(self, year, request):
        self.filter_year = year
        self.request = request
