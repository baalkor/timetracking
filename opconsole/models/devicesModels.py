from django.db import models

class ClientSoftware(models.Model):
    name = models.CharField(max_length=255,unique=True, primary_key=True)
    version = models.CharField(max_length=255,unique=True)
    class Meta:
        unique_together = ('name', 'version')

class Brands(models.Model):
    name =  models.CharField(max_length=255,unique=True)

class DeviceModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey(Brands)
    os = models.ForeignKey(ClientSoftware)
    class Meta:
        unique_together = ('name', 'brand', 'os')