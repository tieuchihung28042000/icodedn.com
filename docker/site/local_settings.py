import os
from django.utils.translation import gettext_lazy as _

# Cấu hình bảo mật
SECRET_KEY = os.environ.get('SECRET_KEY', 'dmoj_docker_secret_key_change_in_production')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

# Cấu hình cơ sở dữ liệu
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

# Cấu hình Redis và Celery
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

# Cấu hình Celery
CELERY_BROKER_URL = f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/0"
CELERY_RESULT_BACKEND = f"redis://{os.environ.get('REDIS_HOST', 'redis')}:6379/0"

# Cấu hình email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Cấu hình ngôn ngữ
LANGUAGE_CODE = 'vi'
DEFAULT_USER_TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Cấu hình tệp tĩnh
STATIC_ROOT = '/app/static'
STATIC_URL = '/static/'
MEDIA_ROOT = '/app/media'
MEDIA_URL = '/media/'

# Cấu hình event server
EVENT_DAEMON_USE = True
EVENT_DAEMON_POST = 'http://localhost:15101/'
EVENT_DAEMON_GET = 'http://localhost:15100/'
EVENT_DAEMON_POLL = 'http://localhost:15102/channels/'
EVENT_DAEMON_KEY = 'event_daemon_key'

# Cấu hình kết nối judge
BRIDGED_JUDGE_ADDRESS = [('bridged', 9999)]
BRIDGED_DJANGO_ADDRESS = [('site', 9998)]
BRIDGED_DJANGO_CONNECT = True

# Cấu hình thư mục bài tập
DMOJ_PROBLEM_DATA_ROOT = '/problems/' 