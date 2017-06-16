from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from opconsole.models.absences import Absences
from opconsole.models.employes import Employes
from django.shortcuts import   get_object_or_404, redirect
from datetime import datetime

class AddAbsence(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        employe = get_object_or_404(Employes,pk=int(request.POST.get("userid")))
        try:
            absence = Absences.objects.create()
            absence.user = employe
            absence.From = datetime.strptime([ request.POST.get("from"), request.POST.get("departure")].join(" "), "%YY-%mm-%dd %H:%M%:%S")
            absence.to = datetime.strptime([ request.POST.get("to"), request.POST.get("arrival")].join(" "), "%YY-%mm-%dd %H:%M%:%S")
            absence.type = request.POST.get("type")
            absence.justification = request.POST.get("justification")
            absence.save()
        except:
            return Response("failed")



        return Response("success")
