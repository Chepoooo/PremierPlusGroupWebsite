from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_default_language(request):
    return redirect(f'/{settings.LANGUAGE_CODE}/')

urlpatterns = [
    path('', redirect_to_default_language),
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('servicios.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
