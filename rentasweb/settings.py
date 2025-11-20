from pathlib import Path
from django.conf import settings
from django.conf.urls.static import static
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _
import dj_database_url

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# 🔐 SECURITY / ENVIRONMENT VARIABLES
# =========================================================
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split()

# =========================================================
# 🔧 APPLICATIONS
# =========================================================
INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminsortable2',
    'servicios',
]

# =========================================================
# 🔧 MIDDLEWARE
# =========================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Required for Railway
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rentasweb.urls'

# =========================================================
# 🔧 TEMPLATES
# =========================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rentasweb.wsgi.application'

# =========================================================
# 🗄 DATABASE (Railway uses DATABASE_URL automatically)
# =========================================================
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=False
    )
}

# =========================================================
# 🔐 PASSWORD VALIDATION
# =========================================================
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# =========================================================
# 🌎 INTERNATIONALIZATION
# =========================================================
LANGUAGES = [
    ('es', _('Español')),
    ('en', _('English')),
    ('fr', _('Français')),
]

LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

MODELTRANSLATION_DEFAULT_LANGUAGE = 'es'
MODELTRANSLATION_TRANSLATE_ADMIN = False

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# =========================================================
# 📁 STATIC & MEDIA FILES
# =========================================================
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =========================================================
# 🔑 DEFAULT PRIMARY KEY
# =========================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
