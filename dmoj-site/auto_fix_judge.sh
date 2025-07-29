#!/bin/bash

echo "🔧 Tự động khắc phục lỗi Judge cho DMOJ..."
echo "=========================================="

# Kiểm tra containers
echo "📋 Kiểm tra trạng thái containers..."
docker compose ps

# Khởi động judge nếu chưa chạy
echo ""
echo "🚀 Khởi động Judge container..."
docker compose up -d judge

# Đợi judge khởi động
echo "⏳ Đợi Judge khởi động..."
sleep 5

# Cập nhật judge trong database
echo ""
echo "💾 Cập nhật Judge trong database..."
docker compose exec site python manage.py shell -c "
from judge.models import Judge, Problem
judge = Judge.objects.first()
if judge:
    judge.online = True
    judge.is_blocked = False
    judge.save()
    print('✅ Đã cập nhật judge online')
    
    # Gán judge cho tất cả problems
    problems = Problem.objects.all()
    for problem in problems:
        if judge not in problem.judges.all():
            problem.judges.add(judge)
    print(f'✅ Đã gán judge cho {problems.count()} problems')
else:
    print('❌ Không tìm thấy judge')
"

# Kiểm tra kết quả
echo ""
echo "🔍 Kiểm tra kết quả..."
docker compose exec site python manage.py shell -c "
from judge.models import Judge, Problem
j = Judge.objects.first()
p = Problem.objects.first()
print(f'Judge: {j.name}, Online: {j.online}, Problems: {j.problems.count()}')
print(f'Problem: {p.name}, Judges: {p.judges.count()}')
"

# Kiểm tra website
echo ""
echo "🌐 Kiểm tra website..."
if curl -s http://localhost:8000/problems/ | grep -q "no judge"; then
    echo "❌ Vẫn còn lỗi 'No judge is available'"
else
    echo "✅ Không còn lỗi 'No judge is available'"
fi

echo ""
echo "🎉 Hoàn tất khắc phục Judge!"
echo "==========================================" 