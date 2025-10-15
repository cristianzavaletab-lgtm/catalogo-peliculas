import os
from pathlib import Path

# ------------------------------------------------------------
# CONFIGURACIÓN BÁSICA
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-tu-clave-secreta-aqui-para-examen'

DEBUG = True

ALLOWED_HOSTS = []

# ------------------------------------------------------------
# APLICACIONES INSTALADAS
# ------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'catalogo',
]

# ------------------------------------------------------------
# MIDDLEWARE (añadiremos WhiteNoise después)
# ------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ------------------------------------------------------------
# CONFIGURACIÓN DE URL Y WSGI
# ------------------------------------------------------------
ROOT_URLCONF = 'peliculas_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'peliculas_project.wsgi.application'

# ------------------------------------------------------------
# BASE DE DATOS (SQLite para desarrollo rápido)
# ------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ------------------------------------------------------------
# CONFIGURACIÓN OPCIONAL PARA MYSQL (COMENTADA)
# ------------------------------------------------------------
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'catalogo_peliculas',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""

# ------------------------------------------------------------
# VALIDADORES DE CONTRASEÑAS
# ------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------
# CONFIGURACIÓN REGIONAL
# ------------------------------------------------------------
LANGUAGE_CODE = 'es-pe'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------
# ARCHIVOS ESTÁTICOS Y MEDIA
# ------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------
# CONFIGURACIÓN PARA PRODUCCIÓN (Render u otros servidores)
# ------------------------------------------------------------
if 'RENDER' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['.onrender.com', 'localhost', '127.0.0.1']
    
    # Archivos estáticos en producción
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
    # Middleware actualizado con WhiteNoise
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- necesario para servir estáticos
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]
    
    # WhiteNoise: optimiza los archivos estáticos
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
