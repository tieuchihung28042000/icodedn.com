#!/bin/bash
set -e

# Đợi database sẵn sàng
echo "Đang đợi database..."
while ! nc -z ${MYSQL_HOST} 3306; do
  sleep 1
done
echo "Database đã sẵn sàng!"

# Tạo time zone data
echo "Cập nhật time zone data..."
mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -h ${MYSQL_HOST} -u ${MYSQL_USER} -p${MYSQL_PASSWORD} mysql || echo "Không thể cập nhật time zone data, tiếp tục..."

# Chuẩn bị static files
echo "Thu thập static files..."
python manage.py collectstatic --noinput || echo "Không thể thu thập static files, tiếp tục..."

# Chuẩn bị translations
echo "Biên dịch translations..."
python manage.py compilemessages || echo "Không thể biên dịch messages, tiếp tục..."
python manage.py compilejsi18n || echo "Không thể biên dịch jsi18n, tiếp tục..."

# Chạy migrations
echo "Chạy migrations..."
python manage.py migrate --noinput

# Kiểm tra nếu cần tạo superuser
echo "Kiểm tra superuser..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print('Superuser đã được tạo')
else:
    print('Superuser đã tồn tại')
"

# Tải dữ liệu ban đầu
echo "Tải dữ liệu ban đầu..."
python manage.py loaddata navbar || true
python manage.py loaddata language_all || true
python manage.py loaddata demo || true

# Khởi động uwsgi
echo "Khởi động DMOJ site..."
exec uwsgi --ini uwsgi.ini 