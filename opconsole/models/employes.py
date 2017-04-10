from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from zones import Zones
class Employes(models.Model):

    id       = models.AutoField(primary_key=True)
    address  = models.CharField(max_length=255)
    city     = models.CharField(max_length=255)
    country  = models.CharField(max_length=255)
    zip_code = models.IntegerField()

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    zones   = models.ManyToManyRel(Zones)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Employes.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()