from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("name/", views.myname, name="myname"),
    path("age/", views.myage, name="myage"),
    path("group/", views.mygroup, name="mygroup"),
    path("common/", views.mycommon, name="mycommon"),
]

