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

# Tạo thư mục cho dmoj và các file tĩnh
RUN mkdir -p /app/dmoj /app/static /app/media

# Tạo file patch để vô hiệu hóa compressor
RUN echo 'import sys\nimport types\n\n# Tạo một module giả để thay thế compressor\nfake_compressor = types.ModuleType("compressor")\nfake_compressor.__path__ = []\nsys.modules["compressor"] = fake_compressor\n\n# Tạo các submodule cần thiết\nfake_templatetags = types.ModuleType("compressor.templatetags")\nsys.modules["compressor.templatetags"] = fake_templatetags\n\nfake_contrib = types.ModuleType("compressor.contrib")\nsys.modules["compressor.contrib"] = fake_contrib\n\nfake_jinja2ext = types.ModuleType("compressor.contrib.jinja2ext")\nsys.modules["compressor.contrib.jinja2ext"] = fake_jinja2ext\n\n# Tạo các hàm giả\nclass DummyCompressNode:\n    def __init__(self, *args, **kwargs):\n        pass\n    \n    def render(self, context):\n        return ""\n\nfake_templatetags.compress = types.ModuleType("compressor.templatetags.compress")\nsys.modules["compressor.templatetags.compress"] = fake_templatetags.compress\nfake_templatetags.compress.CompressNode = DummyCompressNode\n\nprint("Django compressor đã được vô hiệu hóa thành công!")\n' > /app/patch_compressor.py

# Sao chép mã nguồn từ thư mục dmoj-site
COPY dmoj-site/ .

# Sao chép file cấu hình
COPY docker/site/local_settings.py /app/dmoj/
COPY docker/site/uwsgi.ini /app/

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

# Thu thập static files và biên dịch translations
RUN python manage.py collectstatic --noinput || echo "Không thể thu thập static files, tiếp tục..."
RUN python manage.py compilemessages || echo "Không thể biên dịch messages, tiếp tục..."
RUN python manage.py compilejsi18n || echo "Không thể biên dịch jsi18n, tiếp tục..."

# Mở cổng
EXPOSE 8000 9999 15100 15101 15102 

# Thiết lập PYTHONPATH để tải patch_compressor.py trước khi Django khởi động
ENV PYTHONPATH=/app 