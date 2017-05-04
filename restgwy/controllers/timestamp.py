from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from django.shortcuts import   get_object_or_404, redirect
from opconsole.models.devices import Device
from rest_framework.views import APIView
from Crypto.Cipher import AES
import pickle
import base64

class TimestampReciever(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, *args, **kwargs):

        timestps = {}
        for key, entry in request.POST.items():
            timestps[base64.b64decode(key)] = base64.b64decode(entry)


        print timestps





        return HttpResponse()