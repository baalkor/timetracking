from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from opconsole.models.timesheets import Timesheets




@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class StatisticsView(TemplateView):
    template_name = "opconsole_statistics.html"
    model =  Timesheets

    


