from django.db import models
from employes import Employes

E_TYPE = (
    (0, 'SICKNESS'),
    (1, 'HOLIDAY'),
    (2, 'MOVING')
)

class Absences(models.Model):
    user = models.ForeignKey(Employes)
    From = models.DateTimeField()
    to = models.DateTimeField()
    type = models.CharField(max_length=1, choices=E_TYPE)
    justification = models.TextField(blank=True)
    accepted = models.BooleanField(default=False)

