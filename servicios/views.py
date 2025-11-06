from django.shortcuts import render
from .models import Servicio
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def vehiculos(request):
    servicios_list = Servicio.objects.filter(categoria='vehiculo', disponible=True)
    paginator = Paginator(servicios_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'vehiculos.html', {'page_obj': page_obj})

def apartamentos(request):
    servicios_list = Servicio.objects.filter(categoria='apartamento', disponible=True)
    paginator = Paginator(servicios_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'apartamentos.html', {'page_obj': page_obj})

def botes(request):
    servicios_list = Servicio.objects.filter(categoria='bote', disponible=True)
    paginator = Paginator(servicios_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'botes.html', {'page_obj': page_obj})

def paquetes(request):
    servicios_list = Servicio.objects.filter(categoria='paquete', disponible=True)
    paginator = Paginator(servicios_list, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'paquetes.html', {'page_obj': page_obj})