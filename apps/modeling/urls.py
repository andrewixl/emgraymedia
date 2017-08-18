from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^book$', views.book),
    url(r'^contact$', views.contact),
    url(r'^account$', views.account),
    url(r'^modeling$', views.modeling),
    url(r'^photography$', views.photography),
    url(r'^collaborations$', views.collaborations),
    url(r'^createcontact$', views.createcontact),
    url(r'^email$', views.emailclient),
]
