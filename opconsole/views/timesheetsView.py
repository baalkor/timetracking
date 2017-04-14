from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import  login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from opconsole.models import Timesheets
from django.contrib.auth.mixins import UserPassesTestMixin


class TestIsMyTimestampOrStaff(UserPassesTestMixin):
    def test_func(self, request, timeid):
        return self.request.user.is_staff() or \
            Timesheets.object.get(pk=timeid).user.user == self.request.user



@method_decorator(login_required, name='dispatch')
class TimesheetList(ListView):
    template_name = "opconsole_timesheets_list.html"
    model = Timesheets



@method_decorator(login_required, name='dispatch')
class TimestampDetail(TestIsMyTimestampOrStaff, DetailView):
    model = Timesheets
    template_name = "opconsole_timestamp.html"