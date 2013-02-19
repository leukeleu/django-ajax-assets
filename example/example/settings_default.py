import os

import django.conf.global_settings as DEFAULT_SETTINGS

DEBUG = False
TEMPLATE_DEBUG = DEBUG
ADMINS = ()
MANAGERS = ADMINS

DATABASES = {}

SECRET_KEY = 'i_!&$f5@^%y*i_qa$*o&0$3q*1dcv^@_-l2po8-%_$_gwo+i-l'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = DEFAULT_SETTINGS.STATICFILES_FINDERS

ROOT_URLCONF = 'example.urls'
WSGI_APPLICATION = 'example.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'ajax_assets',
    'my_site',
)

LOGIN_REDIRECT_URL = '/'
