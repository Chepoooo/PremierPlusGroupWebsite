from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),# 👈 ruta principal
    path('vehiculos/', views.vehiculos, name='vehiculos'),
    path('apartamentos/', views.apartamentos, name='apartamentos'),
    path('botes/', views.botes, name='botes'),
    path('paquetes/', views.paquetes, name='paquetes'),
]