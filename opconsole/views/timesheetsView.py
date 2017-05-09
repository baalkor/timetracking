from django.views.generic import ListView, DetailView
from opconsole.models.devices import E_STATUS
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from opconsole.models import Timesheets, Employes, Device
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
    model = Timesheets

    def get_context_data(self, **kwargs):
        employee = get_object_or_404(Employes,user=self.request.user)
        hasWebDevice = Device.objects.filter(owner=employee).filter(devType='1').exists()
        context = super(TimesheetView, self).get_context_data(**kwargs)
        context["hasWebDevice"] = hasWebDevice
        context["STATUS"] = E_STATUS
        return context

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