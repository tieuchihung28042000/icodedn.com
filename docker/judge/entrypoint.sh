#!/bin/bash
set -e

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