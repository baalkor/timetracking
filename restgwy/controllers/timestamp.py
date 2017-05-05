from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from opconsole.models.timesheets import Timesheets, TIMB_STATUS
from rest_framework.views import APIView
import pickle
import base64
import pytz
import datetime

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
                    timestamp.status = 0 if deviceData and inZone else  2
                elif self.doDeviceCheck(device) and not self.doGeolocCheck(device):
                    timestamp.status = 0 if deviceData else  2
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


        eTms = Timesheets()
        eTms.time = datetime.datetime.fromtimestamp(
            float(timestps["time"]) / 1000 ,
            pytz.timezone(timestps["timezone"])
        ).strftime('%Y-%m-%d %H:%M:%S')
        eTms.device = dev

        eTms.devKey = timestps["devKey"]
        eTms.user = dev.owner
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