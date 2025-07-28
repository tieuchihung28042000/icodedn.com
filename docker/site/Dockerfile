FROM python:3.10-slim

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    git gcc g++ make python3-dev libxml2-dev libxslt1-dev zlib1g-dev gettext curl \
    default-libmysqlclient-dev redis-server supervisor netcat-openbsd pkg-config \
    libmariadb-dev mariadb-client \
    && curl -sL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g sass postcss-cli postcss autoprefixer \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Tạo thư mục làm việc
WORKDIR /app

# Sao chép mã nguồn từ thư mục dmoj-site
COPY dmoj-site/ .

# Cài đặt các phụ thuộc Python
RUN pip install --no-cache-dir -r requirements.txt
RUN MYSQLCLIENT_CFLAGS="-I/usr/include/mariadb" MYSQLCLIENT_LDFLAGS="-L/usr/lib/x86_64-linux-gnu -lmariadb" pip install --no-cache-dir mysqlclient
RUN pip install --no-cache-dir uwsgi

# Cài đặt các phụ thuộc Node.js
RUN cd websocket && npm install qu ws simplesets
RUN pip install --no-cache-dir websocket-client

# Tạo file cấu hình websocket
RUN echo 'module.exports = { \
    get_host: "0.0.0.0", \
    get_port: 15100, \
    post_host: "0.0.0.0", \
    post_port: 15101, \
    http_host: "0.0.0.0", \
    http_port: 15102, \
    long_poll_timeout: 29000, \
};' > websocket/config.js

# Biên dịch tài nguyên tĩnh
RUN ./make_style.sh

# Tạo thư mục cho tệp tĩnh và media
RUN mkdir -p /app/static /app/media

# Sao chép file cấu hình
COPY docker/site/local_settings.py dmoj/local_settings.py
COPY docker/site/uwsgi.ini .
COPY docker/site/entrypoint.sh .

# Phân quyền cho entrypoint
RUN chmod +x entrypoint.sh

# Mở cổng
EXPOSE 8000 9999 15100 15101 15102

# Khởi chạy
ENTRYPOINT ["/app/entrypoint.sh"] 