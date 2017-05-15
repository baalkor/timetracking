from django.db import models
from django.db.models import ForeignKey, DateField, IntegerField
from employes import Employes

class ActivityRateHistory(models.Model):

    user = ForeignKey(Employes)
    startDate = DateField()
    endDate = DateField(blank=True)
    activityRate = IntegerField(default=100)

