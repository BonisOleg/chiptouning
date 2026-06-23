import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

from .base import *  # noqa: F401,F403

_is_render = 'RENDER' in os.environ

SECRET_KEY = os.environ.get('SECRET_KEY')
if not SECRET_KEY:
    if _is_render:
        raise ImproperlyConfigured(
            'SECRET_KEY environment variable must be set in production.'
        )
    SECRET_KEY = 'django-insecure-local-dev-only-do-not-use-in-production'

DEBUG = not _is_render

ALLOWED_HOSTS = list(ALLOWED_HOSTS)
ALLOWED_HOSTS.extend(['.onrender.com'])
render_external_hostname = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if render_external_hostname:
    ALLOWED_HOSTS.append(render_external_hostname)

CSRF_TRUSTED_ORIGINS = list(CSRF_TRUSTED_ORIGINS)
CSRF_TRUSTED_ORIGINS.append('https://*.onrender.com')
if render_external_hostname:
    CSRF_TRUSTED_ORIGINS.append(f'https://{render_external_hostname}')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    *MIDDLEWARE[1:],
]

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        conn_max_age=600,
    )
}

WHITENOISE_MAX_AGE = 31536000

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}

EMAIL_BACKEND = (
    'django.core.mail.backends.console.EmailBackend'
    if DEBUG
    else 'django.core.mail.backends.smtp.EmailBackend'
)

if _is_render:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
