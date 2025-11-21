import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

load_dotenv()
DEBUG = os.getenv("DEBUG") == "True"
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------
# SECURITY
# -----------------------------
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

ALLOWED_HOSTS = [
    'web-production-ec74c.up.railway.app',
    'www.premierplusgroup.com',
    'premierplusgroup.com',
    '127.0.0.1',
    'localhost'
]

CSRF_TRUSTED_ORIGINS = [
    os.getenv("CSRF_ORIGIN", ""),  # Railway domain
    "https://premierplusgroup.com",
    "https://www.premierplusgroup.com",
]

# -----------------------------
# APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary
    'cloudinary',
    'cloudinary_storage',

    # Tu app
    'servicios',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rentasweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rentasweb.wsgi.application'

# -----------------------------
# DATABASE — Railway PostgreSQL
# -----------------------------
#print("DATABASE_URL:", os.getenv("DATABASE_URL"))
if DEBUG:
    print("➡ Usando base de datos PUBLICA para desarrollo local")
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL_PUBLIC"),
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    print("➡ Usando base de datos INTERNA desde Railway")
    DATABASES = {
        "default": dj_database_url.config(
            default=os.getenv("DATABASE_URL"),
            conn_max_age=600,
            ssl_require=True
        )
    }


# Internacionalización
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('English')),
    ('fr', _('Français')),
]

LANGUAGE_CODE = 'es'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_TRANSLATE_ADMIN = False
LOCALE_PATHS = [BASE_DIR / 'locale']

SESSION_COOKIE_SECURE = True   # obligatorio si usas HTTPS
CSRF_COOKIE_SECURE = True
# -----------------------------
# STATIC FILES
# -----------------------------
# STATIC FILES
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# -----------------------------
# MEDIA — Cloudinary
# -----------------------------
CLOUDINARY_URL = os.getenv("CLOUDINARY_URL")

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

MEDIA_URL = '/media/'

# -----------------------------
# DEFAULT PRIMARY KEY
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
