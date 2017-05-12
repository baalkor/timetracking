from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import Context
from opconsole.models import Timesheets, Device, Employes
from django.db.models import Count
class AnomaliesView(TemplateView):
    template_name = "opconsole_anomalies.html"

    def get(self, request, *args, **kwargs):
        # All the timestamp per user and group by day-mont-year
   #     timesheetsOddTimestamps = Timesheets.objects.values("user","recptTime" ).filter(status='0',recptTime__month__gte=2016 ).annotate(odd=Count("id") % 2).filter(odd=False)

       # print timesheetsOddTimestamps
        return render(request, self.template_name, {"oddtms" : ""})