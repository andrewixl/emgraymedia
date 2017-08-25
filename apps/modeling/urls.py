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
    url(r'^packagedetails/(?P<package_id>\d+)$', views.package),
    url(r'^album/(?P<album_id>\d+)$', views.album),
    url(r'^editprofile$', views.editprofile),
    url(r'^editprofiledata$', views.editprofiledata),
    url(r'^promotions$', views.promotions),
]
