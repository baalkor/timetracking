from .devices import Device, E_STATUS
from employes import Employes
from zones import Zones
from timesheets import Timesheets
from employement_history import ActivityRateHistory
from absences import Absences, E_TYPE
from employes import Employes



from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=Absences)
def check_date_consistency(sender, instance,*args, **kwargs):
    if instance.From > instance.to:
        raise RuntimeError("From greater than to!")

    if instance.accepted:
        if instance.type == 1:
            instance.user.holidaysAnnualCount -= instance.to - instance.From
