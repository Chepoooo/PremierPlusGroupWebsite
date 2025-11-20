from django.db import models
from django.utils import timezone
from django.db.models import Min, Max
import json

class Servicio(models.Model):
    CATEGORIAS = [
        ('vehiculo', 'Renta de Vehículos'),
        ('apartamento', 'Renta de Apartamentos'),
        ('bote', 'Renta de Botes'),
        ('paquete', 'Paquetes Turísticos'),
    ]

    TIPOS_VEHICULO = [
        ('suv', 'SUV'),
        ('compacto', 'Compacto'),
        ('sedan', 'Sedan'),
        ('exclusive', 'Exclusive'),
        ('family', 'Family'),
        ('descapotable', 'Descapotable'),
        ('otro', 'Otro'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    tipo_vehiculo = models.CharField(
        max_length=20,
        choices=TIPOS_VEHICULO,
        blank=True,
        null=True
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.ImageField(upload_to='servicios/')
    disponible = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['fecha_creacion']  # Cambié a fecha_creacion, ya no usamos 'order'

    def __str__(self):
        return self.titulo


class ImagenServicio(models.Model):
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='servicios/imagenes/')
    order = models.PositiveIntegerField(default=0)  # ← NUEVO

    class Meta:
        ordering = ['order']   # ← IMPORTANTE

    def __str__(self):
        return f"{self.servicio.titulo} - Imagen"


class FAQ(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Pregunta Frecuente"
        verbose_name_plural = "Preguntas Frecuentes"
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.pregunta
