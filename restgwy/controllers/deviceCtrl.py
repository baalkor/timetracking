from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from serializers import TempCodeSerializer
from opconsole.models.employes import Employes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

import string
import random


class DeviceRemoval(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        dev = get_object_or_404(Device,pk=int(request.POST.get("id")))
        dev.delete()
        return redirect("/devices/")


class PhoneInit(APIView):
    def post(self, request, *args, **kwargs):
        raise NotImplemented

class WebbrowserInit(APIView):
    def post(self, request, *args, **kwargs):
        raise NotImplemented

class InitProcess(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    TEMP_CODE_MAX_LEN=6
    TEMP_CODE_VALID_DURATION_S=600

    def genTempCode(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(self.TEMP_CODE_MAX_LEN))

    def get(self, request, format=None):
        employee = get_object_or_404(Employes, pk=int(request.GET.get("employeeId")))
        device = Device()
        device.owner = employee
        device.status = 2
        device.devType = int(request.GET.get("typeId"))
        device.tempCode = self.genTempCode()
        device.save()

        serializer = TempCodeSerializer(device)
        return JsonResponse(serializer.data)

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


