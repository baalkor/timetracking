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

    def post(self, request, *args, **kwargs):
        employe = get_object_or_404(Employes,pk=int(request.POST.get("userid")))
        fromStr = " ".join([request.POST.get("from"),request.POST.get("departure")])
        toStr   = " ".join([request.POST.get("to")  , request.POST.get("arrival")] )
        absence = Absences(
            user = employe,
            From = datetime.strptime(fromStr, "%Y-%m-%d %H:%M:%S"),
            to = datetime.strptime(  toStr,   "%Y-%m-%d %H:%M:%S"),
            type = request.POST.get("type"),
            justification=request.POST.get("absense_justification")
        )
        absence.save()


        return Response("success")

class ApproveAbsenceRequest(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


    def post(self, request, *args, **kwargs):
        absence = get_object_or_404(Absences, pk=int(request.POST.get("id")))
        absence.accepted = True
        absence.save()

        return Response()


class RejectAbsenceRequest(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        absence = get_object_or_404(Absences, pk=int(request.POST.get("id")))
        absence.delete()

        return Response()
