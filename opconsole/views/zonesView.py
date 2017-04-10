from django.views.generic import  ListView, DetailView
from opconsole.models.zones import Zones

class ZoneView(ListView):

    template_name = "opconsole_zones.html"
    model = Zones


class ZoneDetailView(DetailView):
    template_name = "opconsole_zone.html"
    model = Zones





