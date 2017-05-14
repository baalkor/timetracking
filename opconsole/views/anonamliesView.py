from django.views.generic import ListView
from opconsole.models import Timesheets, Device, Employes
from django.db.models import Count, F, Q
from django.db.models.functions import Extract
from django.conf import settings
from django.shortcuts import get_object_or_404

class AnomaliesView(ListView):
    template_name = "opconsole_anomalies.html"
    model = Timesheets
    context_object_name = 'anomalies'



    def get_context_data(self, **kwargs):
        context = super(AnomaliesView , self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        isContentAdmin = self.request.user.groups.filter(name=settings.ADMIN_GROUP).exists()
        currUser = get_object_or_404(Employes, user__id=self.request.user.id)

        if isContentAdmin:
            addFilter = Q()
        else:
            addFilter = Q(user=currUser)


        querySet = Timesheets.objects.values(
            "user__user__last_name",
            "user__user__first_name",
            "user__id"
        ).annotate(
            year=Extract("recptTime", "year"),
            month=Extract("recptTime", "month"),
            day=Extract("recptTime", "day")
        ).filter(status='0').annotate(
            nbTimb=Count("day")
        ).annotate(
            odd=F("nbTimb") % 2
        ).filter(odd=True).filter(addFilter)


        return querySet

