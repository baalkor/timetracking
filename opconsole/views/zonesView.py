from django.views.generic import  ListView
from opconsole.models.zones import Zones


class ZoneView(ListView):

    template_name = "opconsole_zones.html"
    model = Zones

