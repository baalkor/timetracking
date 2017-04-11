from opconsole.forms.newUserForm import AddressUserForm, UserCreationFormLocal
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from opconsole.models.employes import Employes
from django.contrib.auth.models import User
from django.db import IntegrityError

class ListUsers(ListView):
    template_name = "opconsole_list_users.html"
    model =  Employes

    class Meta:
        proxy = True

class NewUserView(TemplateView):
    template_name = "opconsole_new_user.html"
    def get(self, request):
        userfrm = UserCreationFormLocal()
        addrfrm = AddressUserForm()
        return render(request, self.template_name,{"user_form":userfrm,"address_form":addrfrm})

    def post(self,request):
        data = request.POST;
        userData = {
            'username':data.get("username"),
            'first_name' : data.get("first_name"),
            'last_name' :data.get("last_name"),
            'password1':data.get("password1"),
            'password2':data.get("password2"),
            'email': data.get("email"),
        }
        addressData = {

            'city':data.get("city"),
            'country':data.get("country"),
            'address':data.get("address"),
            'zip_code':int(data.get("zip_code"))
        }

        userFrom = UserCreationFormLocal(userData)
        addfrm = AddressUserForm(addressData)

        if userFrom.is_valid() and addfrm.is_valid():
            print userData["first_name"]
            django =  User.objects.create_user(username=userData["username"],
                                               email=userData["email"],
                                               password=userData["password1"],
                                               first_name=userData["first_name"],
                                               last_name=userData["last_name"]
                                               )
            employe = Employes(city=addressData["city"],address=addressData["address"],
                               country=addressData["country"], zip_code=addressData["zip_code"], user=django)
            employe.save()
            return redirect("/user/")
        else:
            return render(request, self.template_name,{"user_form":userFrom,"address_form":addfrm} )