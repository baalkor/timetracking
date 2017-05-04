from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse, Http404
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from serializers import TempCodeSerializer, SupercookieSerializer, DeviceSerializer, ZonesListSerializer
from opconsole.models.employes import Employes
from opconsole.models.zones import Zones
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

import string
import random

class ZonesByDevId(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        device = get_object_or_404(Device, pk=int(request.GET.get("id")))
        zonesJSon = ZonesListSerializer(Zones.objetcs.filter(device__id=device.id))
        return zonesJSon.data

class DeviceStatusToggle(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        dev = get_object_or_404(Device,pk=int(request.POST.get("id")))
        if dev.status == '1':
            dev.status = '0'
        else:
            dev.status = '1'

        dev.save()
        return HttpResponse()

class DeviceInfo(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        if request.GET.get("id") is None:
            return Http404
        else:
            dev = get_object_or_404(Device, pk=int())
            serializer = DeviceSerializer(dev)
            return JsonResponse(serializer.data)

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

        pData = request.POST


        dev = get_object_or_404(Device, pk=int(pData.get("deviceId")))
        empId = get_object_or_404(Employes, pk=int(pData.get("employeeId")))

        if dev.tempCode == pData.get("tempCode"):
            dev.deviceData = pData.get("deviceData")
            dev.timezone = pData.get("timezone")
            dev.serial = pData.get("serial")
            dev.phoneNumber = pData.get("phoneNumber")
            dev.status = 0
            dev.save()
            serializer = SupercookieSerializer(dev)
            return JsonResponse(serializer.data);
        else:
            return HttpResponseBadRequest()



