import os
from django.conf import settings
import dj_database_url

DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = settings.DATABASES

DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWADED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_ROOT = "staticfiles"
STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(os.path.join(BASE_DIR, "static")),
)

SECRET_KEY = 'CanIHazS3cret?Meis1337'