import datetime
from django.conf import settings
from opconsole.models import Employes
from django.shortcuts import get_object_or_404


def get_request_or_fallback(request, key, fallback_value, convertFunc=int, checkId=False):
    try:
        if checkId and not isContentAdmin(request):
            return fallback_value
        value = request.GET.get(key)

        if value == None :
            return fallback_value
        else:
            return  convertFunc(value)


    except (ValueError, TypeError):
        return fallback_value



def get_date_or_now(request):
    try:
        date = datetime.datetime.strptime(request.GET.get('date'), "%Y-%m-%d")
    except ( ValueError , TypeError ):
        date = datetime.datetime.now()
    finally:
        return date
def isContentAdmin(request):return request.user.groups.filter(name=settings.ADMIN_GROUP).exists()

def get_employee_or_request(request):
    try:

        uid = int(request.GET.get('userId'))


        myId = uid == request.user

        isNotAllowedCheckingAnotherUserTMS = not myId and not isContentAdmin(request)

        if uid == None or isNotAllowedCheckingAnotherUserTMS:
            emp = get_object_or_404(Employes, user=request.user)
        else:
            emp = get_object_or_404(Employes, pk=uid)
        return emp
    except (TypeError, ValueError):
        return get_object_or_404(Employes, user=request.user)