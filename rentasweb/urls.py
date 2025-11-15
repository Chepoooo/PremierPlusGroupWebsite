from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

# 👇 Ruta para manejar el cambio de idioma
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),   

    # 👇 EL ADMIN DEBE ESTAR AFUERA DEL i18n_patterns
    path('admin/', admin.site.urls),
]

# 🌍 Rutas que SÍ tendrán prefijos por idioma (/es/, /en/, /fr/)
urlpatterns += i18n_patterns(
    path('', include('servicios.urls')),   # Tu app principal
)

# 📁 Archivos multimedia en modo DEBUG
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)