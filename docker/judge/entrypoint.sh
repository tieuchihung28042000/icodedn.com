#!/bin/bash
set -e

# Tạo file judge.yml nếu chưa có
if [ ! -f /problems/judge.yml ]; then
    echo "Tạo file judge.yml..."
    cat > /problems/judge.yml << EOF
id: judge1
key: verysecretkey
problem_storage_globs:
  - /problems/*

runtime:
  gcc: /usr/bin/gcc
  g++: /usr/bin/g++
  g++11: /usr/bin/g++
  python: /usr/bin/python3
  python3: /usr/bin/python3
  java: /usr/bin/java
  javac: /usr/bin/javac
EOF
fi

# Sử dụng biến môi trường để cấu hình judge
if [ ! -z "$JUDGE_NAME" ]; then
    sed -i "s/^id:.*$/id: $JUDGE_NAME/" /problems/judge.yml
fi

if [ ! -z "$JUDGE_KEY" ]; then
    sed -i "s/^key:.*$/key: $JUDGE_KEY/" /problems/judge.yml
fi

# Đợi bridge sẵn sàng
echo "Đang đợi bridge trên $BRIDGE_ADDRESS:$BRIDGE_PORT..."
while ! nc -z $BRIDGE_ADDRESS $BRIDGE_PORT; do
  sleep 2
  echo "Đang thử kết nối lại với $BRIDGE_ADDRESS:$BRIDGE_PORT..."
done
echo "Bridge đã sẵn sàng!"

# Khởi động judge
echo "Khởi động DMOJ judge..."
exec dmoj -c /problems/judge.yml $BRIDGE_ADDRESS $BRIDGE_PORT 