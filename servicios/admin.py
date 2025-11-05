
from django.contrib import admin
from .models import Servicio
from django.utils.html import format_html

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
        'precio',  # Rango de precios
        'fecha_creacion',
        RangoPrecioFilter
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