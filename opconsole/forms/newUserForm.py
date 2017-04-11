from django import forms
from opconsole.models.employes import Employes


class AddressUserForm(forms.ModelForm):
    class Meta:
        model = Employes
        fields = ['address', 'zip_code', 'city', 'country']