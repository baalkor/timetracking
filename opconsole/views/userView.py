from opconsole.forms.newUserForm import AddressUserForm, UserCreationFormLocal
from django.shortcuts import redirect, render
from django.views.generic import  ListView
from opconsole.models.employes import Employes
from django.contrib.auth.models import User, Permission
from django.views import View
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group

class ListUsers(ListView):
    template_name = "opconsole_list_users.html"
    model =  Employes

    class Meta:
        proxy = True


class NewUserView(View):
    template_name = "opconsole_new_user.html"

    @never_cache
    @method_decorator(permission_required('opconsole.add_employes', raise_exception=True))
    def get(self, request, *args, **kwargs):
        userfrm = UserCreationFormLocal()
        addrfrm = AddressUserForm()
        return render(request, self.template_name,{"user_form":userfrm,"address_form":addrfrm})

    @never_cache
    @method_decorator(permission_required('opconsole.add_employes', raise_exception=True))
    def post(self, request, *args, **kwargs):
        data = request.POST
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
            'zip_code':int(data.get("zip_code")),
        }

        admin = data.get("admin")

        userFrom = UserCreationFormLocal(userData)
        addfrm = AddressUserForm(addressData)



        if userFrom.is_valid() and addfrm.is_valid():

            django = User.objects.create_user(

                username=userData["username"],
                email=userData["email"],
                password=userData["password1"],
                first_name=userData["first_name"],
                last_name=userData["last_name"]
            )
            employe = Employes(
               city=addressData["city"],
               address=addressData["address"],
               country=addressData["country"],
               zip_code=addressData["zip_code"],
               user=django
            )

            django.groups.add(Group.objects.get(name='employees'))
            if admin:
                django.groups.add(Group.objects.get(name='contentadmin'))
            django.save()
            employe.save()

            cemploye = Employes.objects.get(pk=employe.id)
#
#            assert cemploye.city == employe.city
#            assert cemploye.address == employe.address
#            assert cemploye.country == employe.country
#            assert cemploye.zip_code == employe.zip_code
#            assert cemploye.user.username == employe.user.username
#            assert cemploye.user.email == employe.user.email
#            assert cemploye.user.first_name == employe.user.first_name
#            assert cemploye.user.last_name == employe.user.last_name
#            assert "employees" in [g.name for g in cemploye.user.groups.all()]


            return redirect("/user/")
        else:
            return render(request, self.template_name,{"user_form":userFrom,"address_form":addfrm} )