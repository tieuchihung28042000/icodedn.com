import os
from django.utils.translation import gettext_lazy as _

# Vô hiệu hóa compressor
INSTALLED_APPS = [app for app in INSTALLED_APPS if app != 'compressor']

# Cấu hình đường dẫn static
STATIC_ROOT = '/app/static'
COMPRESS_ROOT = '/app/static'

# Cấu hình debug
DEBUG = True
ALLOWED_HOSTS = ['*']

# Cấu hình cơ sở dữ liệu
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dmoj',
        'USER': 'dmoj',
        'PASSWORD': 'dmojpass',
        'HOST': 'db',
        'PORT': '3306',
    }
}

# Cấu hình Redis
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Cấu hình email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Internationalization
LANGUAGE_CODE = 'vi'
DEFAULT_USER_TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
MEDIA_ROOT = '/app/media'
MEDIA_URL = '/media/'

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