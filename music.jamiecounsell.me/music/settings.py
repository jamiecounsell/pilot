"""
Django settings for music project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR        = os.path.dirname(os.path.dirname(__file__))
SITE_URL        = "http://music.jamiecounsell.com/"
DOWNLOAD_URL    = "download/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'xk9)l$g_)v5!d+*sdj9f$!ihzqq6)6%(2w_axayj#sqq9t2$je'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

THIRD_PARTY_APPS = tuple()

DEFAULT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

CUSTOM_APPS = (
    'albums',
    'users',
    'streams'
)


INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'microdetector.Middleware'
)

ROOT_URLCONF = 'music.urls'

WSGI_APPLICATION = 'music.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'MUSIC',
        'USER': 'web',
        'PASSWORD': 'pF7ZvvE4cxuPZgftiRe',
        'HOST': 'localhost',  
        'PORT': '3306',
    }
}

# Template loaders

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (os.path.join(BASE_DIR,'..', 'albums/templates/'),)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.i18n",
)

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/web/music.jamiecounsell.me/media/'
STATIC_ROOT = '/home/web/music.jamiecounsell.me/static/'


# Image size settings (width, height) in pixels. And size on disk in MB
PX_SIZE_BACKGROUND = (2500, 2500)
MB_SIZE_BACKGROUND = 15
PX_SIZE_COVER_ART  = (500, 500)
MB_SIZE_COVER_ART  = 2

ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'pjpeg']