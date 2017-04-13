"""timetracking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.urlpatterns import format_suffix_patterns
from opconsole.views import *
from restgwy.controllers import *

urlpatterns = [
    url(r'^api/zones/(?P<pk>[0-9]+)/$', ZoneDetail.as_view()),
    url(r'^login*$',                    auth_views.login, {"template_name" : "opconsole_login.html"}, name="login"),
    url(r'^logout/$',                   auth_views.logout, {'next_page': '/'},name='logout'),
    url(r'^admin/',                     admin.site.urls),
    url(r'^zones/new/$',                ZonesEditorView.as_view()),
    url(r'^user/new/$',                 NewUserView.as_view()),

    url(r'^devices/new/$',              NewDeviceView.as_view()),
    url(r'^devices/$',                  ListDeviceView.as_view()),

    url(r'^user/(?P<pk>\w+)/$',         DetailUserView.as_view()),
    url(r'^user/$',                     ListUsers.as_view()),
    url(r'^zones/$',                    ZoneView.as_view()),
    url(r'^zones/(?P<pk>\w+)/$',        ZoneDetailView.as_view()),
    url(r'^$',                          DashboardView.as_view())
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)