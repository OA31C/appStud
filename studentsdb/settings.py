"""
Django settings for studentsdb project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from django.conf import global_settings
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'OA3IC.QV@gmail.com'
EMAIL_HOST_PASSWORD = 'maxim_1997'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PORTAL_URL = 'http://localhost:8000'

# email settings
# please, set here you smtp server details and your admin email
ADMIN_EMAIL = 'adm1n@studentsdb.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'OA3IC.QV@gmail.com'
EMAIL_HOST_PASSWORD = 'maxim_1997'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f34l_wu@b-)ocu*+ueq_*_qy^une_#x!k=)fo-xmd2gpz_uzk8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'students',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'studentsdb.urls'

WSGI_APPLICATION = 'studentsdb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'students_db_user',
        'PASSWORD': 'password',
        'NAME': 'students_db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/
USE_I18N = True

# default language
LANGUAGE_CODE = 'uk'

# enable Django localization
USE_L10N = True

# use zone-aware date objects
USE_TZ = True

# default timezone
TIME_ZONE = 'UTC'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'students/static')
MEDIA_URL = 'static/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'students/static', 'media')
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + ("django.core.context_processors.request",                                                                             "studentsdb.context_processors.students_proc",
                                                                             "students.context_processor.groups_processor",)

LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'students.views.contact_admin': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}