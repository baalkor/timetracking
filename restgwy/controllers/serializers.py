from rest_framework import serializers

class ZoneSerializer(serializers.Serializer):

    name = serializers.CharField()
    x1 =  serializers.FloatField()
    y1 = serializers.FloatField()
    x2 = serializers.FloatField()
    y2 = serializers.FloatField()
    active = serializers.BooleanField(required=False)