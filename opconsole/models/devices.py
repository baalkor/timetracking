from django.db import models
from employes import Employes
from zones import Zones
import hashlib
import os
import datetime

SALT_LEN=14

E_STATUS = (
    (0, 'INITIALIZED'),
    (1, 'DEACTIVATED'),
    (2, 'INSERTED')
)

E_DEV_TYPE = (
    (0, 'SMARTPHONE'),
    (1, 'WEBBROWSER'),
    (2, 'PHONE'),
)
class Device(models.Model):
    name = models.CharField(max_length=255,default="unnamed")
    status = models.CharField(max_length=1, choices=E_STATUS, default=2)
    deviceData = models.CharField(max_length=255)
    serial = models.CharField(blank=True,max_length=255)
    initDate = models.DateTimeField(default=datetime.datetime.now,blank=True)
    timezone = models.CharField(max_length=255)
    owner = models.ForeignKey(Employes,related_name="devices")
    salt = models.CharField(max_length=SALT_LEN)
    devKey = models.CharField(max_length=64)
    phoneNumber = models.CharField(blank=True, max_length=255)
    devType = models.CharField(max_length=1, choices=E_STATUS, default=0)
    tempCode = models.CharField(max_length=7, choices=E_STATUS)
    zones = models.ManyToManyField(Zones)
    enableGeoCheck = models.BooleanField(default=True)
    enableDeviceCheck = models.BooleanField(default=True)
    def save(self, *args, **kwargs):
        if self.status == 2:
            sltFormat = "%Y%d%m%H%M%S"
            iDate = self.initDate.strftime(sltFormat)
            self.salt = iDate.encode("base-64")

        if self.status == 0:
           self.devKey = hashlib.sha256(str(self.salt) + self.deviceData).hexdigest()
           self.tempCode = "used"



        super(Device, self).save(*args, **kwargs)

