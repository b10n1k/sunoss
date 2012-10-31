import os.path
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('', ''),
)

MANAGERS = ADMINS

#variables
EMAIL_HOST = 'localhost'
DEFAULT_FROM_EMAIL = ''
LOGIN_REDIRECT_URL = '/'
SITE_URL = 'https://example.com:8000'
# Path to redirect to on successful login.
LOGIN_REDIRECT_URL = '/'
# Path to redirect to on unsuccessful login attempt.
LOGIN_REDIRECT_URL_FAILURE = '/'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sunossdb',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = ''

MEDIA_ROOT = '/home/j0ni/Documents/HSGR/sunoss/media'
MEDIA_URL = '/media'
ADMIN_MEDIA_PREFIX = '/media/admin/'
SECRET_KEY = ''

TEMPLATE_DIRS = (
     os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'), 
)

FORCE_SCRIPT_NAME = ''
SERVE_MEDIA = True
