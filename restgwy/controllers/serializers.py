from rest_framework import serializers

class TempCodeSerializer(serializers.Serializer):
    tempCode = serializers.CharField(max_length=7)


class ZoneSerializer(serializers.Serializer):

    name = serializers.CharField()
    x1 =  serializers.FloatField()
    y1 = serializers.FloatField()
    x2 = serializers.FloatField()
    y2 = serializers.FloatField()
    active = serializers.BooleanField(required=False)
    color = serializers.IntegerField()