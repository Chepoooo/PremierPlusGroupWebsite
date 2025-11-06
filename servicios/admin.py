
from datetime import datetime
from django.contrib import admin
from .models import Servicio
from .models import Servicio, FAQ
from django.utils.html import format_html
from datetime import timedelta
from django.utils import timezone

class RangoPrecioFilter(admin.SimpleListFilter):
    title = 'Rango de precios'  # Texto que aparece en el panel lateral
    parameter_name = 'rango_precio'

    def lookups(self, request, model_admin):
        return (
            ('bajo', 'Menos de $100'),
            ('medio', 'Entre $100 y $500'),
            ('alto', 'Más de $500'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'bajo':
            return queryset.filter(precio__lt=100)
        if self.value() == 'medio':
            return queryset.filter(precio__gte=100, precio__lte=500)
        if self.value() == 'alto':
            return queryset.filter(precio__gt=500)
        return queryset
    
class FechaCreacionFilter(admin.SimpleListFilter):
    title = 'Fecha de creación'
    parameter_name = 'fecha_creacion_rango'

    def lookups(self, request, model_admin):
        return (
            ('semana', 'Última semana'),
            ('mes', 'Último mes'),
            ('anio', 'Último año'),
        )

    def queryset(self, request, queryset):
        hoy = timezone.now()
        if self.value() == 'semana':
            hace_una_semana = hoy - timedelta(days=7)
            return queryset.filter(fecha_creacion__gte=hace_una_semana)
        if self.value() == 'mes':
            hace_un_mes = hoy - timedelta(days=30)
            return queryset.filter(fecha_creacion__gte=hace_un_mes)
        if self.value() == 'anio':
            hace_un_anio = hoy - timedelta(days=365)
            return queryset.filter(fecha_creacion__gte=hace_un_anio)
        return queryset

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 
        'categoria', 
        'precio', 
        'disponible', 
        'imagen_preview', 
        'fecha_creacion'
    )
    list_filter = (
        'categoria', 
        'disponible',
        'precio',  # Rango de precios,
        RangoPrecioFilter,
        FechaCreacionFilter
    )
    search_fields = ('titulo', 'descripcion')
    list_editable = ('disponible',)
    ordering = ('categoria', 'titulo')
    list_per_page = 10

    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'imagen_preview')

    fieldsets = (
        ('Información general', {
            'fields': ('titulo', 'descripcion', 'categoria', 'precio', 'disponible')
        }),
        ('Imagen', {
            'fields': ('imagen', 'imagen_preview'),
        }),
        ('Fechas de control', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
        }),
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width: 70px; height: 70px; object-fit: cover; border-radius: 6px;" />', 
                obj.imagen.url
            )
        return "Sin imagen"
    imagen_preview.short_description = 'Vista previa'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'activo', 'fecha_creacion')
    list_filter = ('activo',)
    search_fields = ('pregunta', 'respuesta')