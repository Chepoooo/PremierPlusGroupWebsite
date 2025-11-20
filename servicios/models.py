from django.db import models
from django.db.models import Min

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

    # Campo para ordenar
    order = models.IntegerField(default=0)  # ← Cambiado a IntegerField

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.id:
            # Nuevo servicio → insertarlo al principio
            min_order = Servicio.objects.aggregate(Min('order'))['order__min']
            if min_order is None:
                min_order = 0
            self.order = min_order - 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
