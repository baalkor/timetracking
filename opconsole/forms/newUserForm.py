from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from opconsole.models.employes import Employes

class UserCreationFormLocal(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class AddressUserForm(ModelForm):
    class Meta:
        model = Employes
        fields = ['address', 'zip_code', 'city', 'country']