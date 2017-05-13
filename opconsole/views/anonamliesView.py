from django.views.generic import ListView
from django.shortcuts import render
from django.template import Context
from opconsole.models import Timesheets, Device, Employes
from django.db.models import Count
from itertools import groupby
from django.db.models.functions import Extract

class AnomaliesView(ListView):
    template_name = "opconsole_anomalies.html"
    model = Timesheets
    context_object_name = 'anomalies'

    _dbg_query = ""

    def get_context_data(self, **kwargs):
        context = super(AnomaliesView , self).get_context_data(**kwargs)
        context["query"] = self._dbg_query
        return context

    def get_queryset(self):
        querySet = Timesheets.objects.values(
            "user__user__last_name",
            "user__user__first_name",
            "user__user__id"
        ).annotate(
            year=Extract("recptTime", "year"),
            month=Extract("recptTime", "month"),
            day=Extract("recptTime", "day")
        ).annotate(
            nbTimb=Count("day")
        ).all()
        self._dbg_query = querySet.query
        return querySet

