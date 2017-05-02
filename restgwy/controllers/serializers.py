from rest_framework import serializers

class SupercookieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    devKey = serializers.CharField(max_length=64)

class TempCodeSerializer(serializers.Serializer):
    id  = serializers.IntegerField()
    initDate = serializers.DateTimeField()
    tempCode = serializers.CharField(max_length=7)

class DeviceSerializer(serializers.Serializer):
    id  = serializers.IntegerField()
    initDate = serializers.DateTimeField()
    tempCode = serializers.CharField(max_length=7)
    devKey = serializers.CharField(max_length=64)
    status = serializers.CharField(max_length=1)
    deviceData = serializers.CharField(max_length=255)
    serial = serializers.CharField(max_length=255)
    initDate = serializers.DateTimeField()
    timezone = serializers.CharField(max_length=255)
    owner = serializers.StringRelatedField()
    devKey = serializers.CharField(max_length=64)
    phoneNumber = serializers.CharField(max_length=255)
    devType = serializers.CharField(max_length=1)

class ZoneSerializer(serializers.Serializer):

    name = serializers.CharField()
    x1 =  serializers.FloatField()
    y1 = serializers.FloatField()
    x2 = serializers.FloatField()
    y2 = serializers.FloatField()
    active = serializers.BooleanField(required=False)
    color = serializers.IntegerField()