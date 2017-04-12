from django.db import models

class Zones(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255, unique=True)
    x1   = models.FloatField()
    y1   = models.FloatField()
    x2   = models.FloatField()
    y2   = models.FloatField()
    active = models.BooleanField(default=True)
    color = models.IntegerField(default=16711180)