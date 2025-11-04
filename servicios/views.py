
from django.shortcuts import render
from .models import Servicio

def home(request):
    servicios = Servicio.objects.all()
    context = {
        'categorias': {
            'vehiculos': servicios.filter(categoria='vehiculo'),
            'apartamentos': servicios.filter(categoria='apartamento'),
            'botes': servicios.filter(categoria='bote'),
            'paquetes': servicios.filter(categoria='paquete'),
        }
    }
    return render(request, 'home.html', context)