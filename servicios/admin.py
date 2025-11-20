# Importar translations primero
from .translation import *

from datetime import timedelta
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TranslationAdmin
from .models import Servicio, FAQ

# === Filtros personalizados ===
class RangoPrecioFilter(admin.SimpleListFilter):
    title = 'Rango de precios'
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
            return queryset.filter(fecha_creacion__gte=hoy - timedelta(days=7))
        if self.value() == 'mes':
            return queryset.filter(fecha_creacion__gte=hoy - timedelta(days=30))
        if self.value() == 'anio':
            return queryset.filter(fecha_creacion__gte=hoy - timedelta(days=365))
        return queryset

# === Admin Servicio ===
@admin.register(Servicio)
class ServicioAdmin(SortableAdminMixin, TranslationAdmin):
    list_display = (
        'order',
        'titulo',
        'categoria',
        'tipo_vehiculo',
        'precio',
        'disponible',
        'imagen_preview',
        'fecha_creacion'
    )
    list_display_links = ('titulo',)
    list_filter = (
        'categoria',
        'tipo_vehiculo',
        'disponible',
        RangoPrecioFilter,
        FechaCreacionFilter
    )
    search_fields = ('titulo', 'descripcion')
    list_editable = ('disponible',)
    list_per_page = 10
    ordering = ['order']  # asegura que adminsortable2 funcione correctamente

    readonly_fields = ('fecha_creacion', 'fecha_actualizacion', 'imagen_preview')

    fieldsets = (
        ('Mover', {
            'fields': ('order',),
        }),
        ('Información general', {
            'fields': ('titulo', 'descripcion', 'categoria', 'tipo_vehiculo', 'precio', 'disponible')
        }),
        ('Imagen principal', {
            'fields': ('imagen', 'imagen_preview'),
        }),
        ('Fechas de control', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
        }),
    )

    def imagen_preview(self, obj):
        if obj.imagen:
            return format_html(
                '<img src="{}" style="width:70px; height:70px; object-fit:cover; border-radius:6px;" />',
                obj.imagen.url
            )
        return "Sin imagen"
    imagen_preview.short_description = 'Vista previa'

# === Admin FAQ ===
@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('pregunta', 'activo', 'fecha_creacion')
    list_filter = ('activo',)
    search_fields = ('pregunta', 'respuesta')
