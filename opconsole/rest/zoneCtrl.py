from opconsole.rest.serializers import ZoneSerializer
from opconsole.models.zones import Zones
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ZoneDetail ( RetrieveUpdateDestroyAPIView ):

    queryset = Zones.objects.all()
    serializer_class = ZoneSerializer
