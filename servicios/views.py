from django.shortcuts import render
from .models import Servicio

def home(request):
    return render(request, 'home.html')

def vehiculos(request):
    servicios = Servicio.objects.filter(categoria='vehiculo', disponible=True)
    return render(request, 'vehiculos.html', {'servicios': servicios})

def apartamentos(request):
    servicios = Servicio.objects.filter(categoria='apartamento', disponible=True)
    return render(request, 'apartamentos.html', {'servicios': servicios})

def botes(request):
    servicios = Servicio.objects.filter(categoria='bote', disponible=True)
    return render(request, 'botes.html', {'servicios': servicios})

def paquetes(request):
    servicios = Servicio.objects.filter(categoria='paquete', disponible=True)
    return render(request, 'paquetes.html', {'servicios': servicios})