"""
Django settings for misitio project.

Generated by 'django-admin startproject' using Django 1.11.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7y=8r8$c8^858m0htoe#p$nhzhj5x(14@j3e9br2_lru_shyhn'
#se usa para manejar la base de datos.


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#es para ver los errores mientras estamos viendo la aplicacion
#cuando el programa este en produccion se pone en false para que no pueda ver los errores
ALLOWED_HOSTS = ['edxh92.pythonanywhere.com','127.0.0.1']
#definimos las direcciones ips que pueden ver nuestra aplcacion por default esta vacia.
#se define queines se pueden conectar

# Application definition
#las apps son todos los modulos que el programa trae, trae dos aplicaciones un area donde se publican los blos
#otra es donde se ponden los demas
INSTALLED_APPS = [
    'material',
    'material.frontend',
    'material.admin',
    'django.contrib.admin',#administramos la aplciacion,
    'django.contrib.auth',#nos permite tener la autenticacion
    'django.contrib.contenttypes',#permite subir archivos y descargar archivos
    'django.contrib.sessions',#trae la aplicacion para manejar sessiones
    'django.contrib.messages',#nos permite enviar mensajes de errores o tener bien todo
    'django.contrib.staticfiles',#para desplejar los logos o cualquier otra cosa
    'blog',
    #si los archivos no tiesudo apt-get install paper-gtk-themene coma da errores,
]
#son aplicaciones intermedias entre dos partes del programa para autenticar los usarios
#permite manejar seguridad, sesiones,
#estas aplicaciones ejecutan codigo en dos partes de nuestra aplicacion
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#nos dice cual es la primera pagina donde va abuscar las direcciones
ROOT_URLCONF = 'misitio.urls'#busca las urles de cada una de las paginas.
#son las plantillas que trae para poder trabajar default
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
#aplicacion wsgi es el que se comunica con el servidor web
WSGI_APPLICATION = 'misitio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

#definimos que base de datos vamos a emplear
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators
#autenticaciones para las contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
    #esto es para tener contrasñas sencillas.
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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#se configura el lenguaje en que va estar la aplcaicon
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-gt'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'America/Guatemala'


USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
#es para tener el css y el JavaScript
STATIC_ROOT=os.path.join(BASE_DIR,'static')
