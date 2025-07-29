#!/bin/bash
set -e

# Chạy migrations
python manage.py migrate

# Chạy bridge daemon trong background
echo "Khởi động bridge daemon..."
python manage.py runbridged &
BRIDGE_PID=$!

# Đợi bridge daemon khởi động
echo "Đợi bridge daemon khởi động..."
sleep 5

# Kiểm tra bridge daemon có chạy không
if ! kill -0 $BRIDGE_PID 2>/dev/null; then
    echo "Bridge daemon không chạy được!"
    exit 1
fi

echo "Bridge daemon đã khởi động với PID: $BRIDGE_PID"

# Chạy Django server
echo "Khởi động Django server..."
python manage.py runserver 0.0.0.0:8000

# Đợi bridge daemon kết thúc
wait $BRIDGE_PID 