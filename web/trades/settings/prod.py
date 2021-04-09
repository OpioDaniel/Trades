from .base import *

DEBUG = False

ADMINS = (
    ('Amos Baranes', 'amos@DrBaranes.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

MEDIA_ROOT = '/usr/src/app/media/'  # for nginx
STATIC_ROOT = '/usr/src/app/static/'  # for nginx
