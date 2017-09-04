from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^error$', views.error),
    url(r'^(?P<number>\w+)$', views.show),
    url(r'^(?P<number>\d+)$', views.show),
]