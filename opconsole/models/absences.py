from django.db import models
from employes import Employes

class Absences(models.Model):
    user = models.ForeignKey(Employes)
    From = models.DateTimeField()
    to = models.DateTimeField()
    type = models.IntegerField()
    justification = models.TextField(blank=True)

