"""
Django settings for JobApplicationSystem project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from decouple import config
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_numeric_filter',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'job',
    'application',
    'django_summernote',
    'bootstrap_datepicker_plus',
    'bootstrap4',
    'admin_auto_filters',
    'extra_views',
    'crispy_forms',
    'interview',
    'smart_selects',
    'djangoql',
    'import_export',
    'django_admin_filter',
    'fieldsets_with_inlines',
    'django_cleanup.apps.CleanupConfig',






]
USE_DJANGO_JQUERY = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'JobApplicationSystem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'JobApplicationSystem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {

    "default": {
        "ENGINE": "mssql",
        "NAME": "JBDB",
        "USER": "sa",
        "PASSWORD":  config('SQLPASS'),
        "HOST": "sqlserver",
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
        },
    },



    #'default': {

       # 'ENGINE': 'django.db.backends.postgresql_psycopg2',

       # 'NAME': 'JADB',

      #  'USER': 'aref',

      #  'PASSWORD': 'a',

      #  'HOST': 'localhost',

     #   'PORT': '5432',

   # }

}
DATABASE_CONNECTION_POOLING = False
#{
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}

# Email Config

#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'mail.sukhtian.com.jo'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587 
#EMAIL_HOST_USER = 'hr@sukhtian.com.jo'
#EMAIL_HOST_PASSWORD = config('EMAILPASS')




# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(TEMPLATES_DIR, 'static')] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
  
# allows to load iframe from same hostname
X_FRAME_OPTIONS = "SAMEORIGIN"
SUMMERNOTE_THEME = 'bs4'

DEFAULT_AUTO_FIELD='django.db.models.AutoField' 