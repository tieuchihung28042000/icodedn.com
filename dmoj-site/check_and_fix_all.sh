#!/bin/bash

echo "🔍 Kiểm tra và khắc phục toàn bộ hệ thống DMOJ..."
echo "=================================================="

# Kiểm tra containers
echo "📋 Kiểm tra trạng thái containers..."
docker compose ps

# Kiểm tra website
echo ""
echo "🌐 Kiểm tra website..."
if curl -s http://localhost:8000/ > /dev/null; then
    echo "✅ Website đang hoạt động"
else
    echo "❌ Website không hoạt động"
    exit 1
fi

# Kiểm tra lỗi judge
echo ""
echo "🔍 Kiểm tra lỗi judge..."
if curl -s http://localhost:8000/problems/ | grep -q "no judge"; then
    echo "❌ Phát hiện lỗi 'No judge is available'"
    echo "🔧 Đang khắc phục..."
    ./dmoj-site/auto_fix_judge.sh
else
    echo "✅ Không có lỗi judge"
fi

# Kiểm tra judge trong database
echo ""
echo "💾 Kiểm tra judge trong database..."
docker compose exec site python manage.py shell -c "
from judge.models import Judge, Problem
j = Judge.objects.first()
p = Problem.objects.first()
print(f'Judge: {j.name}, Online: {j.online}, Problems: {j.problems.count()}')
print(f'Problem: {p.name}, Judges: {p.judges.count()}')
"

# Kiểm tra trang problem
echo ""
echo "📝 Kiểm tra trang problem..."
if curl -s -L http://localhost:8000/problem/aplusb/ | grep -q "Submit solution"; then
    echo "✅ Trang problem có nút Submit solution"
else
    echo "❌ Trang problem không có nút Submit solution"
fi

# Kiểm tra judge container
echo ""
echo "⚙️ Kiểm tra judge container..."
if docker compose ps | grep -q "judge.*Up"; then
    echo "✅ Judge container đang chạy"
else
    echo "❌ Judge container không chạy"
    echo "🔧 Đang khởi động judge..."
    docker compose up -d judge
fi

# Tóm tắt
echo ""
echo "📊 Tóm tắt trạng thái:"
echo "======================"
echo "🌐 Website: $(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/)"
echo "🗄️ Database: $(docker compose ps | grep db | grep -o 'healthy')"
echo "⚡ Redis: $(docker compose ps | grep redis | grep -o 'healthy')"
echo "⚙️ Judge: $(docker compose ps | grep judge | grep -o 'Up')"
echo "🌍 Site: $(docker compose ps | grep site | grep -o 'Up')"

echo ""
echo "🎉 Kiểm tra hoàn tất!"
echo "==================================================" 