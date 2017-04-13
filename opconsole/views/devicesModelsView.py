from opconsole.models.devicesModels import Brands, ClientSoftware, DeviceModel
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

class BaseView(object):
    template_name = "opconsole_generic_edit_form.html"
    success_url = reverse_lazy('device_model_list')

    class Meta:
        abstract = True

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class BrandsList(ListView, BaseView):
    template_name = "opconsole_brands_list.html"
    model = Brands

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class BrandsCreate(BaseView, CreateView):
    model = Brands
    fields = ['name']

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class BrandsUpdate(UpdateView):
    model = Brands
    fields = ['name']
@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class BrandsDelete(DeleteView):
    model = Brands
@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ClientSoftwareList(ListView, BaseView):
    model = ClientSoftware
    template_name = "opconsole_clientsoftware_list.html"

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ClientSoftwareCreate(BaseView, CreateView):
    model = ClientSoftware
    fields = ['name', 'version']

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ClientSoftwareUpdate(BaseView, UpdateView):
    model = ClientSoftware
    fields = ['name', 'version']

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class ClientSoftwareDelete(BaseView,DeleteView):
    model = ClientSoftware

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class DeviceModelList(ListView, BaseView):
    template_name = "opconsole_devicemodel_list.html"
    model = DeviceModel

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class DeviceModelCreate(BaseView,CreateView):
    model = DeviceModel
    fields = ['brand', 'name', 'os']

@method_decorator(permission_required('opconsole.add_employes', raise_exception=True), name='dispatch')
class DeviceModelUpdate(BaseView,UpdateView):
    model = DeviceModel
    fields = ['brand', 'name', 'os']

class DeviceModelDelete(BaseView,DeleteView):
    model = DeviceModel

