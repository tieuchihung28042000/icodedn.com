#!/bin/bash

echo "Sửa lỗi 'No judge is available for this problem'..."

# Cập nhật judge thành online
docker compose exec site python manage.py shell -c "
from judge.models import Judge, Problem
judge = Judge.objects.first()
if judge:
    judge.online = True
    judge.is_blocked = False
    judge.save()
    print('Đã cập nhật judge online')
    
    # Gán judge cho tất cả problems
    problems = Problem.objects.all()
    for problem in problems:
        if judge not in problem.judges.all():
            problem.judges.add(judge)
    print(f'Đã gán judge cho {problems.count()} problems')
else:
    print('Không tìm thấy judge')
"

echo "Hoàn tất!" 