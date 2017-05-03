from django.shortcuts import   get_object_or_404, redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from opconsole.models.employes import Employes
from rest_framework.views import APIView

class UserToggle(APIView):

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(Employes,pk=int(request.POST.get("id")))
        user.enable = not user.enable
        user.save()
        return redirect("/user/")

