from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render




class DashboardView(PermissionRequiredMixin, TemplateView):
    template_name = "opconsole_dashboard.html"
    permission_required = 'opconsole.add_employes'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
