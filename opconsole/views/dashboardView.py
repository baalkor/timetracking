from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from opconsole.models import Device, Employes
import datetime


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "opconsole_dashboard.html"

    def get(self, request, *args, **kwargs):
        employee = Employes.objects.filter(user=self.request.user)
        hasWebDevice =  Device.objects.filter(owner=employee).filter(devType='1').count() == 0

        return render(request, self.template_name, {"hasWebDevice":hasWebDevice,"time":datetime.datetime.now()})
