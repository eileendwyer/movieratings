"""movieratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from movieratings_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#    url(r'^$', views.test_view),
    url(r'^$', views.home, name='home'),
    url(r'^averagerating/$', views.averagerating, name='averagerating'),
    url(r'^rater_info/$', views.rater_info, name='rater_info'),


]
