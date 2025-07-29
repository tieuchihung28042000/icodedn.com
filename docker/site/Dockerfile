FROM python:3.10-slim

# Cài đặt các gói cần thiết cơ bản
RUN apt-get update && apt-get install -y \
    git gcc g++ make python3-dev libxml2-dev libxslt1-dev zlib1g-dev gettext curl \
    default-libmysqlclient-dev netcat-openbsd pkg-config \
    libmariadb-dev mariadb-client \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Tạo thư mục cho dmoj và các file tĩnh
RUN mkdir -p /app/dmoj /app/static /app/media

# Sao chép mã nguồn từ thư mục dmoj-site
COPY dmoj-site/ .

# Cài đặt các tool frontend cần thiết cho make_style.sh
RUN apt-get update && apt-get install -y npm && \
    npm install -g sass postcss-cli autoprefixer && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài đặt các dependencies Python từ requirements.txt của dmoj-site
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir pymoss

# Vô hiệu hóa compressor trong settings.py và jinja2 extension
RUN sed -i "s/'compressor',/# 'compressor',/g" dmoj/settings.py && \
    sed -i "/'compressor.contrib.jinja2ext.CompressorExtension',/d" dmoj/settings.py && \
    echo "STATIC_ROOT = '/app/static'" >> dmoj/settings.py && \
    echo "COMPRESS_ROOT = '/app/static'" >> dmoj/settings.py && \
    echo "COMPRESS_ENABLED = False" >> dmoj/settings.py

# Tạo file local_settings.py nếu chưa có
RUN echo "DEBUG = True" > dmoj/local_settings.py && \
    echo "ALLOWED_HOSTS = ['*']" >> dmoj/local_settings.py && \
    echo "DATABASES = {'default': {'ENGINE': 'django.db.backends.mysql', 'NAME': 'dmoj', 'USER': 'dmoj', 'PASSWORD': 'dmojpass', 'HOST': 'db'}}" >> dmoj/local_settings.py && \
    echo "CACHES = {'default': {'BACKEND': 'django_redis.cache.RedisCache', 'LOCATION': 'redis://redis:6379/1'}}" >> dmoj/local_settings.py && \
    echo "SESSION_ENGINE = 'django.contrib.sessions.backends.cache'" >> dmoj/local_settings.py

# Sao chép script startup
COPY docker/site/start.sh /start.sh
RUN chmod +x /start.sh

# Mở cổng
EXPOSE 8000 9998 9999

# Thiết lập entrypoint
CMD ["/start.sh"] 