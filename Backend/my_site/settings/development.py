from my_site.settings.common import *


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4(^j0(j1_w*t77+_8(mqhj45cz5u$1t5-i9c$uehi1bu$z*5w)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# CORS
CORS_ALLOW_ALL_ORIGINS = True

# CSRF
CSRF_TRUSTED_ORIGINS = ['http://localhost',
                        'http://127.0.0.1',
                        'https://localhost',
                        'https://127.0.0.1',
                        'https://s15-20-n-python-react.onrender.com']


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
