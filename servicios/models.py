
from django.db import models

class Servicio(models.Model):
    CATEGORIAS = [
        ('vehiculo', 'Renta de Vehículos'),
        ('apartamento', 'Renta de Apartamentos'),
        ('bote', 'Renta de Botes'),
        ('paquete', 'Paquetes Turísticos'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    imagen = models.ImageField(upload_to='servicios/')
    disponible = models.BooleanField(default=True)
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.titulo