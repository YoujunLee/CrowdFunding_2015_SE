# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
"""
Django settings for djangoproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
'''
여기는 그냥 서버 관리 하는 곳이라서 특별한일 없으면 안건드리셔도 됩니다.

'''
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(_rjnznla)xcivk4)yh9v)xd2wa8m4^+4+bc#%9xy6&axu&cui'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'write',
    'TossAPI',
    'View'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangoproject.urls'

WSGI_APPLICATION = 'djangoproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'soft',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'bitnami'
      
      }
}
DATABASE_OPTIONS={
    'unix_socket' : '/tmp/mysql.sock',
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/



STATIC_ROOT = '/opt/bitnami/apps/django/django_projects/djangoproject/funding/'

STATIC_URL = '/funding/'

STATICFILES_DIRS = (
('css', '/opt/bitnami/apps/django/django_projects/djangoproject/funding/css'),
('js', '/opt/bitnami/apps/django/django_projects/djangoproject/funding/js'),
('html','/opt/bitnami/apps/django/django_projects/djangoproject/funding/html'),

)

TEMPLATE_DIRS = (
    ('/opt/bitnami/apps/django/django_projects/djangoproject/funding/'),
)

TEMPLATE_LOADERS = (
    "django_mobile.loader.Loader",
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader")


