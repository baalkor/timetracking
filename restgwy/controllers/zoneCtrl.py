from .serializers import  ZoneSerializer
from django.shortcuts import   get_object_or_404
from rest_framework.response import Response
from opconsole.models.zones import Zones
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class ZoneDetail ( RetrieveDestroyAPIView ):

    queryset = Zones.objects.all()
    serializer_class = ZoneSerializer

class ZoneToggle(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        zone = get_object_or_404(Zones,pk=int(request.POST.get("id")))
        zone.active = not zone.active
        zone.save()
        return Response()