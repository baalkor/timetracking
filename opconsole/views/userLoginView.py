from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from opconsole.forms.loginForm import LoginForm


class UserLoginView(TemplateView):
    template_name = "opconsole_login.html"
    user = None
    def get(self, request):
        if not request.user.is_authenticated:
            form = LoginForm()
            return render(request,  self.template_name, form)
        else:
            return redirect("/")

    def post(self, request):
        username , password = ( request.POST['username'], request.POST['password'] )
        user = authenticate(username=username, password=password)
        if user is None:
            return redirect("/login", self.template_name)