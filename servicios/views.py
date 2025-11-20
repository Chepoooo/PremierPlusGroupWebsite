from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Servicio, FAQ


def home(request):
    faqs = FAQ.objects.filter(activo=True)
    return render(request, 'home.html', {'faqs': faqs})


def filtrar_servicios(request, categoria, incluir_tipo=False):
    """Vista reutilizable para aplicar filtros y paginación en todos los servicios."""
    servicios = Servicio.objects.filter(categoria=categoria, disponible=True)

    # --- FILTRO DE TIPO (solo para vehículos) ---
    tipo = request.GET.get('tipo')
    if incluir_tipo and tipo:
        servicios = servicios.filter(tipo_vehiculo=tipo)

    # --- FILTROS DE PRECIO ---
    precio_min = request.GET.get('precio_min')
    precio_max = request.GET.get('precio_max')

    if precio_min:
        try:
            servicios = servicios.filter(precio__gte=float(precio_min))
        except ValueError:
            pass

    if precio_max:
        try:
            servicios = servicios.filter(precio__lte=float(precio_max))
        except ValueError:
            pass

    # --- PAGINACIÓN ---
    paginator = Paginator(servicios, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'precio_min': precio_min,
        'precio_max': precio_max,
    }

    if incluir_tipo:
        context['tipo_seleccionado'] = tipo

    return context


# ===== VISTAS INDIVIDUALES =====

def vehiculos(request):
    context = filtrar_servicios(request, 'vehiculo', incluir_tipo=True)
    return render(request, 'vehiculos.html', context)


def apartamentos(request):
    context = filtrar_servicios(request, 'apartamento')
    return render(request, 'apartamentos.html', context)


def botes(request):
    context = filtrar_servicios(request, 'bote')
    return render(request, 'botes.html', context)


def paquetes(request):
    context = filtrar_servicios(request, 'paquete')
    return render(request, 'paquetes.html', context)

