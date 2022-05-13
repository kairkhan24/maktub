# TODO: always check for "python manage.py check --deploy"
import os
from pathlib import Path

from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY: str = config('SECRET_KEY', cast=str)
DEBUG: bool = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SIDE_APPS = [

]

PROJECT_APPS = [
    'apps.blog.apps.BlogConfig',
]

INSTALLED_APPS = [
    *DJANGO_APPS,
    *SIDE_APPS,
    *PROJECT_APPS,
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "ATOMIC_REQUESTS": config("ATOMIC_REQUESTS", cast=bool, default=False),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT", cast=int),
        "CONN_MAX_AGE": config("CONN_MAX_AGE", cast=int, default=60),
        "OPTIONS": {
            "connect_timeout": 10,
            "options": "-c statement_timeout=15000ms"
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE: str = config("TIME_ZONE", default="Asia/Almaty", cast=str)
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = os.path.join('staticfiles')
MEDIA_URL: str = "/media/"
MEDIA_ROOT: str = os.path.join("media")


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
