from django.db import models
from django.utils import timezone
from opconsole.models import Employes, Device

TIMB_STATUS = (
    (0, 'ACCEPTED'),
    (1, 'REFUSED_WRONG_TZ'),
    (2, 'REFUSED_DEV_DATA_MISMATCH'),
    (3, 'REFUSED_NOT_IN_ZONE'),
    (4, 'USER_DEACTIVATED'),
    (5, 'DEVICE_DEACTIVATED'),
    (6, 'WAITING_APPROVAL')
)

class Timesheets(models.Model):

    user = models.ForeignKey(Employes, related_name="timesheets")
    device = models.ForeignKey(Device, related_name="tms", null=True)
    recptTime = models.DateTimeField(auto_now_add=timezone.now() )
    time = models.DateTimeField()
    devTz = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=1, choices=TIMB_STATUS)
    deletion = models.BooleanField(default=False)




