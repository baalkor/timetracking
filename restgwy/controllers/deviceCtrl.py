from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest
from opconsole.models.devices import Device, E_STATUS
class DeviceInit(APIView):
    def post(self, request, *args, **kwargs):
        try:

            device = Device.create()
            device.timezone = request.POST.get("timezone")
            device.deviceData = request.POST.get("deviceData")
            device.serial = request.POST.get("serial")
            device.owner = request.user
            device.phoneNumber = request.POST.get("phone_number")
            device.save()
            device.status = 0
            device.save()
            return Response("Device initalized")

        except:
            return HttpResponseBadRequest


