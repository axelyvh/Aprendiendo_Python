from django.shortcuts import render
from django.http import HttpResponse

def pacientes(request):
    return HttpResponse("Estas en la pagina de pacientes")