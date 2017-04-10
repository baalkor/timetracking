from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import Context
from django.conf import settings


class ZonesView(TemplateView):
    template_name = "opconsole_zones.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, Context({"google_api_key":settings.GOOGLE_API_KEY}))
