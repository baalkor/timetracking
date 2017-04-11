from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from zones import Zones

class Employes(models.Model):

    address  = models.CharField(max_length=255)
    city     = models.CharField(max_length=255)
    country  = models.CharField(max_length=255)
    zip_code = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="django_user")

    zones   = models.ManyToManyField(Zones)

    def __str__(self):
        return self.id
