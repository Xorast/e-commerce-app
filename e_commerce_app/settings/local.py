from .base import *

SECRET_KEY      = os.environ.get("SECRET_KEY")

DEBUG           = True

ALLOWED_HOSTS   = ["e-commerce-app-pangur.c9users.io"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES       = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL       = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
STATIC_ROOT      = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL        = '/media/'
MEDIA_ROOT       = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND    = 'django.core.mail.backends.console.EmailBackend'
SYSTEM_EMAIL     = 'yourname@example.com'