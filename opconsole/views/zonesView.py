from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.template import Context

import datetime

class ZoneView(TemplateView):
    template_name = "opconsole_zones.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, Context({"time":datetime.datetime.now()}))
