from django.contrib import admin
from django.urls import path
from Tokenapp import views

urlpatterns = [
    path("",views.studentview, name="studentview"),

    path("adminview/",views.adminview,name="adminview"),

    path("token/",views.token,name="token"),

    path("markasresolved/<int:pk>",views.markasresolved,name="markasresolved"),

    path("currenttoken/",views.currenttoken,name="currenttoken"),
]