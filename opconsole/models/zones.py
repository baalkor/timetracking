from django.db import models

class Zones(models.Model):

    name = models.CharField(max_length=255, unique=True)
    x1   = models.FloatField()
    y1   = models.FloatField()
    x2   = models.FloatField()
    y2   = models.FloatField()