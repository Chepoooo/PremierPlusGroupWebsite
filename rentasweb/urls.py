from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import redirect

# Redirigir la raíz al idioma por defecto
def redirect_to_default_language(request):
    return redirect(f'/{settings.LANGUAGE_CODE}/')

urlpatterns = [
    path('', redirect_to_default_language),  # raíz '/'
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('servicios.urls')),  # rutas de tu app
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
