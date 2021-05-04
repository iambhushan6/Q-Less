from django.contrib import admin
from django.urls import path
from Tokenapp import views

urlpatterns = [
    path("",views.studentview, name="studentview"),
    path("adminview/",views.adminview,name="adminview"),
    path("thanku/",views.thanku,name="thanku")
]