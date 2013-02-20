from settings_default import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'ajax-assets.sqlite',
    }
}

LOGIN_REDIRECT_URL = '/'
