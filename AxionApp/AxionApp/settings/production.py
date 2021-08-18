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
        'NAME': 'd5gjaft3f0lrhd',
        'USER': 'rikhgidwmzfrwi',
        'PASSWORD': 'eac5830bc798f2cd6934c0dc7c13d9311deefcd1ab2071ab73ac0e960f9d4ade',
        'HOST': 'ec2-54-236-234-167.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (BASE_DIR , 'static') 

