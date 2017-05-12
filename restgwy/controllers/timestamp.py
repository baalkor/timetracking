from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseForbidden
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from opconsole.models.employes import Employes
from opconsole.models.timesheets import Timesheets, TIMB_STATUS
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from serializers import TimestampSerializer
from django.conf import settings

import base64
import pytz
import datetime

ALLOWED_MODIFICATION = [ "deletion", "manual"]

class AskTmpsManual(APIView):



    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:

            action = request.POST.get("action")
            if action == None or action not in ALLOWED_MODIFICATION:
                return HttpResponseBadRequest()
            else:
                if action == "deletion":
                    tms = get_object_or_404(Timesheets, pk=int(request.POST.get("id")))
                    tms.deletion = not tms.deletion
                elif action == "manual" :
                    tms = Timesheets(
                        user =  get_object_or_404(Employes,pk=int(request.POST.get("id"))),
                        device=None,
                        time=datetime.datetime.fromtimestamp(
                                    float(request.POST.get("time")) / 1000 ,
                                        pytz.timezone(request.POST.get("timezone"))
                                ).strftime('%Y-%m-%d %H:%M:%S'),
                            devTz=request.POST.get("timezone"),
                        latitude=0.,
                        longitude=0.,
                        status='6'
                    )
                else:
                    return HttpResponseBadRequest()


            tms.save()

            return HttpResponse()
        except (TypeError, ValueError):
            return HttpResponseBadRequest()

class ApproveAskTmpsDeletionManual(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            action = request.POST.get("action")
            if action == None or action not in ALLOWED_MODIFICATION:
                return HttpResponseBadRequest()
            else:
                isContentAdmin = self.request.user.groups.filter(name=settings.ADMIN_GROUP).exists()
                if isContentAdmin:
                    tms = get_object_or_404(Timesheets, pk=int(request.POST.get("id")))
                    if action == "deletion":
                        tms.delete()
                    elif action == "manual":
                        tms.status = 0
                        tms.save()
                    return HttpResponse(status=200)
                else:
                    return HttpResponseForbidden
        except (TypeError, ValueError):
            return HttpResponseBadRequest()

class RejectAskTmpsDeletionManual(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            action = request.POST.get("action")
            if action == None or action not in ALLOWED_MODIFICATION:
                return HttpResponseBadRequest()
            else:
                isContentAdmin = self.request.user.groups.filter(name=settings.ADMIN_GROUP).exists()
                if isContentAdmin:
                    tms = get_object_or_404(Timesheets, pk=int(request.POST.get("id")))
                    if action == "deletion":
                        tms.deletion = False
                        tms.save()
                    elif action == "manual":
                        tms.delete()
                    return HttpResponse(status=200)
                else:
                    return HttpResponseForbidden
        except (TypeError, ValueError):
            return HttpResponseBadRequest()


class TimestampReciever(APIView):
    authentication_classes = ()
    permission_classes = ()

    def isDeviceEnabled(self, device):
        return device.status == '0'

    def isUserEnabled(self, device):
        return device.owner.enable

    def isInZones(self,device, x,y):
        return device.zones.filter(
            x1__lte=x, x2__gte=x,
            y1__lte=y, y2__gte=y
        ).first()




    def doDeviceCheck(self, device):
        return device.enableDeviceCheck

    def doGeolocCheck(self, device):
        return device.enableGeoCheck

    def InspectTimestamp(self, device,timestamp, **kwargs):

        if self.isDeviceEnabled(device):
            if self.isUserEnabled(device):

                inZone = self.isInZones(device, kwargs.pop("longitude"), kwargs.pop("latitude")) != None
                deviceData = device.deviceData ==  kwargs.pop("deviceData")
                deviceTz = device.timezone == kwargs.pop("timezone")

                if self.doDeviceCheck(device) and self.doGeolocCheck(device):
                    timestamp.status = 0 if deviceData and inZone and deviceTz else  2
                elif self.doDeviceCheck(device) and not self.doGeolocCheck(device):
                    timestamp.status = 0 if deviceData and deviceTz else  1
                elif not self.doDeviceCheck(device) and self.doGeolocCheck(device):
                    timestamp.status = 0 if deviceData else 3
                else:
                    timestamp.status = 0
            else:
                timestamp.status = 4
        else:
            timestamp.status = 5



    def post(self, request, *args, **kwargs):

        timestps = {}
        for key, entry in request.POST.items():
            timestps[base64.b64decode(key).encode("utf-8")] = base64.b64decode(entry)
        dev = get_object_or_404(Device, devKey=timestps["devKey"])
#        user = get_object_or_404(Employes, user=request.user)



        eTms = Timesheets()
        eTms.time = datetime.datetime.fromtimestamp(
            float(timestps["time"]) / 1000 ,
            pytz.timezone(timestps["timezone"])
        ).strftime('%Y-%m-%d %H:%M:%S')
        eTms.device = dev
        eTms.devTz = timestps["timezone"]
        eTms.devKey = timestps["devKey"]
        eTms.user = dev.owner # request.user if dev.owner != user else dev.owner
        eTms.latitude = float(timestps["latitude"])
        eTms.longitude = float(timestps["longitude"])

        self.InspectTimestamp(dev,eTms,
                              latitude=float(timestps["latitude"]),
                              longitude=float(timestps["longitude"]),
                              deviceData=timestps["deviceData"],
                              timezone=timestps["timezone"]
        )
        eTms.save()

        return JsonResponse({"code":eTms.status, "status":TIMB_STATUS[eTms.status]})


class TimestampDetailCtrl(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        timestamp = get_object_or_404(Timesheets, pk=int(request.POST.get("id")))
        timestampInfo = TimestampSerializer(timestamp)
        return JsonResponse(timestampInfo.data)