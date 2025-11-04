
# Register your models here.
from django.contrib import admin
from .models import Servicio

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'disponible')
    list_filter = ('categoria', 'disponible')
    search_fields = ('titulo', 'descripcion')