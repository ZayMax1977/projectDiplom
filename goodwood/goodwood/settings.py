"""
Django settings for goodwood project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import datetime
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-69m%8)%!c*)ow02xxb205v!3%&%-36fje*)$h&@gl+3*on9z)q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# APPEND_SLASH=False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news.apps.NewsConfig',
    'chance.apps.ChanceConfig',

    'law.apps.LawConfig',
    'tourism.apps.TourismConfig',
    'adv.apps.AdvConfig',
    'index.apps.IndexConfig',
    'contact.apps.ContactConfig',


]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

]

ROOT_URLCONF = 'goodwood.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
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

WSGI_APPLICATION = 'goodwood.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/



STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = '/media/'

INTERNAL_IPS = [
    '127.0.0.1',
]

# CKEDITOR_UPLOAD_PATH = "uploads/"
#
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': [
#             ['Undo', 'Redo',
#              '-', 'Bold', 'Italic', 'Underline',
#              '-', 'Link', 'Unlink', 'Anchor',
#              '-', 'Format',
#              '-', 'Maximize',
#              '-', 'Table',
#              '-', 'Image',
#              '-', 'Source',
#              '-', 'NumberedList', 'BulletedList'
#             ],
#             ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock',
#              '-', 'Font', 'FontSize', 'TextColor',
#              '-', 'Outdent', 'Indent',
#              '-', 'HorizontalRule',
#              '-', 'Blockquote'
#             ]
#         ],
#         'height': 500,
#         'width': '100%',
#         'toolbarCanCollapse': False,
#         'forcePasteAsPlainText': True
#     }
# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
        ),
    'PAGE_SIZE': 10,
     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
         'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
         # 'rest_framework_simplejwt.authentication.JWTAuthentication',
     ],
    'DEFAULT_PAGINATION_CLASS':'rest_framework_json_api.pagination.PageNumberPagination',
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=3),

    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),
}
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'auth/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': True,
    'SEND_CONFIRMATION_EMAIL': True,

    # 'SERIALIZERS': {},
    'PASWORD_RESET_SHOW_EMAIL_NOT_FOUND': True,
    'TOKEN_MODEL': None,
}
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "zamax77@mail.ru"
EMAIL_HOST_PASSWORD = "Lcr5BXj69Afi0faJv9ei"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
SERVER_EMAIL = "zamax77@mail.ru"
DEFAULT_FROM_EMAIL = "zamax77@mail.ru"

# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'


