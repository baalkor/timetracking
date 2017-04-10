from django.views.generic import TemplateView
from django.shortcuts import render
from django.template import Context
from django.http import HttpResponse
from django.conf import settings
from opconsole.models.zones import Zones


class ZonesEditorView(TemplateView):
    template_name = "opconsole_zones_editor.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, Context({"google_api_key":settings.GOOGLE_API_KEY}))

    def post(self, request):
        zoneDta = request.POST
        Zones(name=zoneDta["name"],
              x1=zoneDta["x1"],
              y1=zoneDta["y1"],
              x2=zoneDta["x2"],
              y2=zoneDta["y2"]).save()

        return  HttpResponse(status=200);
