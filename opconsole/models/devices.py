from django.db import models
from employes import Employes
import hashlib
import os

SALT_LEN=100

E_STATUS = (
    (0, 'INITIALIZED'),
    (1, 'DEACTIVATED'),
    (2, 'INSERTED')
)
class Device(models.Model):
    status = models.CharField(max_length=1, choices=E_STATUS, default=2)
    deviceData = models.CharField(max_length=255)
    serial = models.CharField(max_length=255)
    initDate = models.DateTimeField(blank=True)
    timezone = models.CharField(max_length=255)
    owner = models.ForeignKey(Employes)
    salt = models.IntegerField()
    devKey = models.CharField(max_length=64)
    phoneNumber = models.CharField(blank=True, max_length=255)

    def save(self, *args, **kwargs):
        salt = os.urandom(SALT_LEN)
        devKey = hashlib.sha256( str(salt) + self.serial + self.deviceData ).hexdigest()

        super(models.Model, self)

