from settings_default import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'd-ajax-media',
        'USER': 'user',
        'PASSWORD': 'pass',
        'HOST': '',
        'PORT': '',
    }
}

LOGIN_REDIRECT_URL = '/'
