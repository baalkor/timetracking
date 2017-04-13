from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from opconsole.models.devices import Device

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class NewDeviceView(CreateView):
    model = Device
    fields = ['devModel','serial','owner']
    template_name = "opconsole_add_device.html"

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ListDeviceView(ListView):
    model = Device
    fields = ['status','devModel','serial','owner', 'initDate', 'timezone' ]
    template_name = "opconsole_list_devices.html"

