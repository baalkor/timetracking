from django.db import models
from employes import Employes

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
