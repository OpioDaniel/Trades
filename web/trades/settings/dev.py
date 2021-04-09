from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'trades',
        'USER': 'trades',
        'PASSWORD': 'sql1pass',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
