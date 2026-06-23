import dj_database_url
from decouple import config

from .base import *  # noqa: F401,F403

DEBUG = False

DATABASES = {
    'default': dj_database_url.config(
        default=(
            f"postgres://{config('POSTGRES_USER', default='distage')}:"
            f"{config('POSTGRES_PASSWORD', default='distage')}@"
            f"{config('DB_HOST', default='db')}:"
            f"{config('DB_PORT', default='5432')}/"
            f"{config('POSTGRES_DB', default='distage_db')}"
        ),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# TLS завершується в nginx; Gunicorn працює по HTTP
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = config('USE_HTTPS', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('USE_HTTPS', default=False, cast=bool)

if config('USE_HTTPS', default=False, cast=bool):
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
