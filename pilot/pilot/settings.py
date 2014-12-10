"""
Django settings for Pilot project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dotenv
PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
dotenv.load_dotenv(os.path.join(PROJECT_PATH, ".env"))

BASE_DIR        = os.path.dirname(os.path.dirname(__file__))
SITE_URL        = unicode(os.environ.get("SITE_URL"))
DOWNLOAD_URL    = "download/"

# Let's get dem environment variables

# Django Variable
VAR_DEBUG           = bool(os.getenv("DEBUG", True))
DJANGO_SECRET       = unicode(os.environ.get("DJANGO_SECRET_KEY"))

# Email Variables
VAR_EMAIL_HOST      = unicode(os.environ.get("EMAIL_HOST"))
VAR_EMAIL_PORT      = int(os.environ.get("EMAIL_PORT"))
VAR_EMAIL_USER      = unicode(os.environ.get("EMAIL_HOST_USER"))
VAR_EMAIL_PASSW     = unicode(os.environ.get("EMAIL_HOST_PASSWORD"))
VAR_EMAIL_USE_TLS   = bool(os.environ.get("EMAIL_USE_TLS"))
VAR_DEFAULT_FROM    = unicode(os.environ.get("DEFAULT_FROM_EMAIL"))

VAR_DB_NAME         = unicode(os.environ.get("DB_NAME"))
VAR_DB_USER         = unicode(os.environ.get("DB_USER"))
VAR_DB_PASWORD      = unicode(os.environ.get("DB_PASSWORD"))
VAR_DB_HOST         = unicode(os.environ.get("DB_HOST")) 
VAR_DB_PORT         = unicode(os.environ.get("DB_PORT"))

# Stripe API Key Variables
STRIPE_SECRET_KEY       = unicode(os.environ.get("STRIPE_SECRET"))
STRIPE_PUBLISHABLE_KEY  = unicode(os.environ.get("STRIPE_PUBLISH"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = VAR_DEBUG

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

ROOT_URLCONF = 'pilot.urls'

WSGI_APPLICATION = 'pilot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': VAR_DB_NAME,
        'USER': VAR_DB_USER,
        'PASSWORD': VAR_DB_PASWORD,
        'HOST': VAR_DB_HOST,  
        'PORT': VAR_DB_PORT,
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
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'media'))
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'static'))


# Image size settings (width, height) in pixels. And size on disk in MB
PX_SIZE_BACKGROUND = (2500, 2500)
MB_SIZE_BACKGROUND = 15
PX_SIZE_COVER_ART  = (500, 500)
MB_SIZE_COVER_ART  = 2

ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'pjpeg']

# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = VAR_EMAIL_HOST
EMAIL_PORT = VAR_EMAIL_PORT
EMAIL_HOST_USER = VAR_EMAIL_USER
EMAIL_HOST_PASSWORD = VAR_EMAIL_PASSW
EMAIL_USE_TLS = VAR_EMAIL_USE_TLS
DEFAULT_FROM_EMAIL = VAR_DEFAULT_FROM