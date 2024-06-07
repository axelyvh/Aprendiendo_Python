from django.contrib import admin
from django.urls import path, include
from paciente import views

urlpatterns = [
    path('', views.pacientes, name='paciente'),
]