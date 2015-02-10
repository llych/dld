"""
Django settings for devops project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u)eun!#2q=(@!(rtvry6swiopp3=1d)@6(^omt9^_%w)xjarrs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


import djcelery
djcelery.setup_loader()
BROKER_URL = 'django://'
CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
CELERY_TRACK_STARTED=True

CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT=['json']
#CELERY_RESULT_BACKEND = 'django://'

# Application definition



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'host_management',
    'login_admin',
    'ansible_app',
    'djcelery',
    'kombu.transport.django',
    'code_management',
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

ROOT_URLCONF = 'devops.urls'

WSGI_APPLICATION = 'devops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'devops.db'),
        'NAME': os.path.join(BASE_DIR, '/data/devops.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS=(
os.path.join(os.path.dirname(__file__), '../templates').replace('\\','/'),
#os.path.join(BASE_DIR,'template').replace('\\','/'),

)

HERE = os.path.dirname(os.path.dirname(__file__)) 
MEDIA_ROOT = os.path.join( HERE ,'../media').replace('\\','/') 
MEDIA_URL = '/media/' 
STATIC_ROOT = os.path.join(HERE,'../static').replace('\\','/') 
STATICFILES_DIRS = ( 
   os.path.join(HERE,'static/').replace('\\','/'), 
) 


SESSION_COOKIE_NAME = 'devopsid'
ANSIBLE_TEMP=os.path.join(os.path.dirname(__file__), '../temp').replace('\\','/')
#APPEND_SLASH=False