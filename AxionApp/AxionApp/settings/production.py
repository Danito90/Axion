from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['gestionch.herokuapp.com']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd4d9o1pq2nu1aa',
        'USER': 'vwksauwkbquiua',
        'PASSWORD': '8994df6a2f7f5e1a5603c2d1c6f5da7295c1529cf8ddfbfe221e81bd888ca163',
        'HOST': 'ec2-52-23-190-126.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (BASE_DIR , 'static') 

