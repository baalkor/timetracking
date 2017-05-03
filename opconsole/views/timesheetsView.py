from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from opconsole.models import Timesheets, Employes
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404

class TestIsMyTimestampOrStaff(UserPassesTestMixin):
    def test_func(self, request, timeid):
        return self.request.user.is_staff() or \
            Timesheets.object.get(pk=timeid).user.user == self.request.user


@method_decorator(login_required, name='dispatch')
class TimesheetView(ListView):
    context_object_name = 'timestamps'
    template_name = "opconsole_my_timesheet.html"

    def get_queryset(self):
        employee = Employes.objects.filter(user=self.request.user)
        return Timesheets.objects.filter(user=employee)


@method_decorator(login_required, name='dispatch')
class TimesheetList(ListView):
    template_name = "opconsole_timesheets_list.html"
    model = Timesheets



@method_decorator(login_required, name='dispatch')
class TimestampDetail(TestIsMyTimestampOrStaff, DetailView):
    model = Timesheets
    template_name = "opconsole_timestamp.html"