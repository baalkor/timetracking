from django.views.generic import  ListView, DetailView
from opconsole.models.zones import Zones
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

@method_decorator(permission_required('opconsole.add_zones', raise_exception=True), name='dispatch')
class ZoneView(ListView):

    template_name = "opconsole_zones.html"
    model = Zones

@method_decorator(permission_required('opconsole.add_zones', raise_exception=True), name='dispatch')
class ZoneDetailView(DetailView):
    template_name = "opconsole_zone.html"
    model = Zones





