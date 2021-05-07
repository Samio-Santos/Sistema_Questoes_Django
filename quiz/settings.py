"""
Django settings for quiz project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from django.contrib.messages import constants
from archive import *
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zp0zy!vqe=d08588vg%1m@myhx_&l3c#jqpyn4x^doq4--6ye%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'accounts',
    'categorias',
    'perguntas',
    'respostas',
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',
]

AUTH_USER_MODEL = 'accounts.CostumerUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',

]

ROOT_URLCONF = 'quiz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'quiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = 'static'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "files"),)


# Para o usuario poder adicionar mídias, fazer as configurações abaixo.
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join (BASE_DIR, 'midias/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages
# Os alertas vão na classe da tag no template
MESSAGE_TAGS = {
    constants.INFO: 'alert-info',
    constants.SUCCESS: 'alert-success',
    constants.WARNING: 'alert-warning',
    constants.ERROR: 'alert-error',
    constants.DEBUG: 'alert-info',
}

# Configuração rede social
AUTHENTICATION_BACKENDS = (
    'accounts.backend.EmailUserBackend',
    'axes.backends.AxesBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
)
#### Configurações social auth ####
SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'accounts.social_auth.sucesso'
)

# Autenticação pelo facebook
SOCIAL_AUTH_FACEBOOK_KEY = '414184179999238'
SOCIAL_AUTH_FACEBOOK_SECRET = 'SECRET_KEY_FACEBOOK'

# Autenticação pelo Github
SOCIAL_AUTH_GITHUB_KEY = 'a4a0697de7ac8fb277e2'
SOCIAL_AUTH_GITHUB_SECRET = 'SECRET_KEY_GITHUB'

# Autenticação pelo Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '955161584054-ocobrnmng47tj4625kk4rtsbojqbukjf.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'SECRET_KEY_GOOGLE'

LOGIN_REDIRECT_URL = '/'
LOGOUt_REDIRECT_URL = '/'

##### CONFIGURAÇÕES DO DO AXE #####

# Defini o limite de tentativas do usuario
AXES_FAILURE_LIMIT = 5

# # AXES_ENABLE_ADMIN = True

# Bloqueia com base no nome do usuario
AXES_ONLY_USER_FAILURES = True

# redefini o numero de tentativas após UMA tentativa bem-sucedida
AXES_RESET_ON_SUCCESS = True

# Defini o tempo de bloqueio
AXES_COOLOFF_TIME = timedelta(minutes=30)

# redireciona o usuario para este template quando bloqueado
AXES_LOCKOUT_TEMPLATE = 'accounts_templates/locked.html'


# SMTP configurações

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = EMAIL
EMAIL_HOST_PASSWORD = PASSWORD
EMAIL_TIMEOUT = 60
DEFAULT_FROM_EMAIL = 'Simulados team'
