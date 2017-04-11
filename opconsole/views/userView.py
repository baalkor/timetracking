from django.contrib.auth.forms import UserCreationForm
from opconsole.forms.newUserForm import AddressUserForm
from django.shortcuts import render
from django.views.generic import TemplateView

class NewUserView(TemplateView):
    template_name = "opconsole_new_user.html"
    def get(self, request):
        userfrm = UserCreationForm()
        addrfrm = AddressUserForm()
        return render(request, self.template_name,{"user_form":userfrm,"address_form":addrfrm})