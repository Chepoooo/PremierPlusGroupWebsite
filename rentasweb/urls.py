from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from servicios.views import redirect_to_default_language  # 👈 aquí

urlpatterns = [
    path('', redirect_to_default_language),  # 👈 raíz '/'
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('servicios.urls')),  # rutas de tu app con prefijo de idioma
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render