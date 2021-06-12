from django.contrib import admin
from django.urls import path
from Tokenapp import views

urlpatterns = [
    path("",views.studentview, name="studentview"),

    path("adminview/",views.adminview,name="adminview"),

    path("token/",views.token,name="token"),

    path("markasresolved/<int:pk>",views.markasresolved,name="markasresolved"),

    path("currenttoken/",views.currenttoken,name="alumnicurrenttoken"),


    path("alumniregistration/",views.alumniregistration,name="alumniregistration"),
    
    path("alumniadminview/",views.alumniadminview,name="alumniadminview"),

    path("alumnitoken/",views.alumnitoken,name="alumnitoken"),

    path("alumnimarkasresolved/<int:pk>",views.alumnimarkasresolved,name="alumnimarkasresolved"),

    path("alumnicurrenttoken/",views.alumnicurrenttoken,name="alumnicurrenttoken"),
]