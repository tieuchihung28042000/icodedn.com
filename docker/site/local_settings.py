import os
from django.utils.translation import gettext_lazy as _

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'dmoj_docker_secret_key_change_in_production')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'dmoj'),
        'USER': os.environ.get('MYSQL_USER', 'dmoj'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'dmojpass'),
        'HOST': os.environ.get('MYSQL_HOST', 'db'),
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION',
        },
    }
}

# Caches and sessions
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/1",
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Celery
CELERY_BROKER_URL = f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/0"

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
LANGUAGE_CODE = 'vi'
DEFAULT_USER_TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_ROOT = '/app/static'
STATIC_URL = '/static/'
MEDIA_ROOT = '/app/media'
MEDIA_URL = '/media/'

# django-compressor settings
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_JS_FILTERS = ['compressor.filters.jsmin.JSMinFilter']
COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = STATIC_ROOT

# DMOJ site display settings
SITE_NAME = 'ICODEDN'
SITE_LONG_NAME = 'ICODEDN: Modern Online Judge'
SITE_ADMIN_EMAIL = 'admin@icodedn.com'

# Bridge settings
BRIDGED_JUDGE_ADDRESS = [('bridged', 9999)]
BRIDGED_DJANGO_ADDRESS = [('site', 9998)]
BRIDGED_DJANGO_CONNECT = True

# Event server
EVENT_DAEMON_USE = True
EVENT_DAEMON_POST = 'http://localhost:15101/'
EVENT_DAEMON_GET = 'http://localhost:15100/'
EVENT_DAEMON_POLL = 'http://localhost:15102/channels/'
EVENT_DAEMON_KEY = 'event_daemon_key'

# Problem data
DMOJ_PROBLEM_DATA_ROOT = '/problems/' 