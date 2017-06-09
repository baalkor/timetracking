from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from opconsole.models import Device, Employes
import datetime


@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class DashboardView(TemplateView):
    template_name = "opconsole_dashboard.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
