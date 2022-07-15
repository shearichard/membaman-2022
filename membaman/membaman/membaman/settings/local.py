from os.path import abspath, basename, dirname, join, normpath
from sys import path

from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}