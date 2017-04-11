from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, BooleanField
from opconsole.models.employes import Employes

class UserCreationFormLocal ( UserCreationForm ):
    admin = BooleanField(required=False)
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class AddressUserForm(ModelForm):
    class Meta:
        model = Employes
        fields = ['address', 'zip_code', 'city', 'country']