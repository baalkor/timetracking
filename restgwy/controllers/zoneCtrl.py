from .serializers import  ZoneSerializer
from opconsole.models.zones import Zones
from rest_framework.generics import RetrieveDestroyAPIView

class ZoneDetail ( RetrieveDestroyAPIView ):

    queryset = Zones.objects.all()
    serializer_class = ZoneSerializer
