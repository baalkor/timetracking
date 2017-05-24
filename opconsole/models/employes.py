from django.db import models
from django.contrib.auth.models import User
from zones import Zones

class Employes(models.Model):

    function = models.CharField(max_length=255)
    address  = models.CharField(max_length=255)
    city     = models.CharField(max_length=255)
    country  = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    phone    = models.CharField(max_length=255, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="django_user")
    enable = models.BooleanField(default=True)
    holidaysAnnualCount = models.PositiveIntegerField(default=20)