from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from rest_framework.views import APIView


class TimestampReciever(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        return HttpResponse()