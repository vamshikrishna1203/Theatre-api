"""mytheatre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from managerapp import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls), # admin site
    url(r'^occupy/$', views.Occupy.as_view()),#occupy url endpoint
    #get_info url endpoint which takes ticket_id or name or seat_no
    url(r'^get_info/(?:(?P<seat_no>\d+)|(?P<name>\w+)|(?P<ticket_id>[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89aAbB][a-f0-9]{3}-[a-f0-9]{12}))/$', views.GetPerson.as_view()),
    #vacate url endpoint which takes seat_no
    url(r'^vacate/(?P<seat_no>\d+)/$', views.Vacate.as_view()),

]
