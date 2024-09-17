"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wrj5qm#d@+s0=1f7#ku5#)^u$@251^c@i)$_pu!s$m1zkbv$_i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'corsheaders',
    'drf_yasg',
    'debug_toolbar',
    'rest_framework', 
    'channels',
    'logs',
    'lms_system',
    'community',
    'core',
    "api",
    'gamiflication',

    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
    # 'server.middleware.RoleBasedRedirectMiddleware',
]

ROOT_URLCONF = 'server.urls'

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # Other backends if needed
]




LOGOUT_REDIRECT_URL = '/login/'  

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}

# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'

# WSGI_APPLICATION = 'server.wsgi.application'
ASGI_APPLICATION = 'server.asgi.application'
# SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# settings.py

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379)],  # Redis server location
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




STATICFILES_DIRS = [BASE_DIR,'static']

MEDIA_ROOT = BASE_DIR/'media'
MEDIA_URL = "/media/"

REST_FRAMEWORK = {
    # Set the default pagination class
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    
    # Define the default number of items per page
    'PAGE_SIZE': 10,  # Adjust this number based on your needs

    # Optional: Allow clients to specify page size via query parameter
    'PAGE_SIZE_QUERY_PARAM': 'page_size',

    # Optional: Set a maximum page size to prevent abuse
    'MAX_PAGE_SIZE': 100,

    # Set the default authentication and permission classes
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}




SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),

    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
} 

DJOSER = {
    'SERIALIZERS':{ 
        # 'user_create':'core.serializers.UserCreateSerializer',
        'current_user':'core.serializers.LoginSystemSerializer',
        'user': 'core.serializers.LoginSystemSerializer', 
        
    }

}



AUTH_USER_MODEL ='core.LoginSystem'



CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1",
    "http://127.0.0.1:64120",
]



SWAGGER_SETTINGS = {
    
    'VALIDATOR_URL': 'http://127.0.0.1:8000',
    'SECURITY_DEFINITIONS': {
        'basic': {
            'type': 'basic'
        }
    },

}

REDOC_SETTINGS = {
   'LAZY_RENDERING': False,

}


LOGIN_URL = '/login/?next=/'  # Adjust this URL according to your login page URL




# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'  # Gmail's SMTP server
# EMAIL_PORT = 587  # Port for TLS
# EMAIL_USE_TLS = True  # Use TLS
# EMAIL_USE_SSL = False  # Do not use SSL (use TLS instead)
# EMAIL_HOST_USER = 'satishmh26@gmail.com'  # Your Gmail address
# EMAIL_HOST_PASSWORD = 'gdug zoaf enta zjia'  #    gdug zoaf enta zjia
# DEFAULT_FROM_EMAIL = 'satishmh26@gmail.com'  # Default "From" email address


    
