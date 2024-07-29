from .common import *

INSTALLED_APPS  =  [
   'daphne',
   'drf_spectacular',
] + INSTALLED_APPS


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ashop',
        'USER': 'ashop',
        'PASSWORD': '123@456',
        'HOST': 'db',
        'PORT': '5432',
    }
}