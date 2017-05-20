from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from graphos.sources.model import ModelDataSource
from opconsole.models.timesheets import Timesheets
from graphos.renderers import flot

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class StatisticsView(TemplateView):
    template_name = "opconsole_statistics.html"
    model =  Timesheets
    def get_context_data(self, **kwargs):
        context = super(StatisticsView, self).get_context_data()
        context["workingHours"] = flot.LineChart( ModelDataSource(Timesheets.objects.all(), fields=["time","recptTime"]) )
        return context
