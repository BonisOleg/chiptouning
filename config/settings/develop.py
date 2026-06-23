import dj_database_url
from decouple import config

from .base import *  # noqa: F401,F403

DEBUG = config('DEBUG', default=True, cast=bool)

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

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
