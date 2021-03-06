"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from article import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^date/(?P<date>\d+)$', views.dateGroup, name="dateGroup"),
    url(r'^test/', views.test),
    #url(r'^(?P<parameter>\d+)/$', views.detail, name = 'detail'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^category/(?P<cate>\S+)/$', views.category, name='category'),
    #url(r'^(?P<dateX>[0-9]{4}/[0-9]{2}/[0-9]{2})$', views.dateGroup, name="dateGroup"),


]
