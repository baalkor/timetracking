from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, TemplateView, UpdateView
from opconsole.models.devices import Device
from django.shortcuts import  render, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseBadRequest
from opconsole.models.employes import Employes
from opconsole.models.devices import E_DEV_TYPE


class DeviceDetail(UpdateView):
    template_name = "opconsole_device_details.html"
    model = Device
    fields = ['id','status','deviceData','serial','owner', 'initDate', 'timezone' , 'devKey']

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class NewDeviceView(TemplateView):
    model = Device
    template_name = "opconsole_add_device.html"

    def get(self, request):
        return HttpResponseForbidden()

    def post(self, request):

        data = request.POST.get('id')

        try:
            employee = get_object_or_404(Employes, pk=int(data))
            return render(request, self.template_name, {"employee":employee, "devType":E_DEV_TYPE, "wizardList":[ ( "dialogs/wizard_" + n + ".html", n ) for i,n in E_DEV_TYPE]})
        except TypeError as e:
            print e.message
            return HttpResponseBadRequest()

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ListDeviceView(ListView):
    model = Device
    fields = ['status','deviceData','serial','owner', 'initDate', 'timezone' ]
    template_name = "opconsole_list_devices.html"

