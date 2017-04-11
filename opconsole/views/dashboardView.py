from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import datetime


@method_decorator(login_required, name='dispatch')
class DashboardView(TemplateView):
    template_name = "opconsole_dashboard.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"time":datetime.datetime.now()})
