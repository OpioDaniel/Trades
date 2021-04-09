import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # trades
WEB_DIR = os.path.dirname(BASE_DIR)                                      # web
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))                  # setting

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '5(15ds+i2+%ik6z&!yer+ga9m=e%jcqiz_5wszg)r-z!2--b2d'
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'easy_thumbnails',

    'trades.apps.main',
    'trades.apps.todo',
    'trades.apps.dbillings',
    'trades.apps.gamestore',
    'trades.apps.ugandatowns'
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'trades.middleware.LoginRequiredMiddleware',
)

ROOT_URLCONF = 'trades.urls'

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

WSGI_APPLICATION = 'trades.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"), ]
# print('---STATICFILES_DIRS---')
# print(STATICFILES_DIRS)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_ROOT = os.path.join(WEB_DIR, "static")

AUTH_USER_MODEL = 'main.GlobUser'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/main/login/'
LOGOUT_URL = '/'

LOGIN_EXEMPT_URLS = (
    r'',
    r'^/$',
    r'^main/$',
    r'^logout/$',
    r'^register/$',
    r'^reset-password/complete/$',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'amos@DrBaranes.com'
EMAIL_HOST_PASSWORD = 'Amos122#'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
