#!/usr/bin/env python
"""
Script quản lý judge trong DMOJ
"""
import os
import sys
import django

# Thêm đường dẫn project vào sys.path
sys.path.append('/app')

# Thiết lập Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')
django.setup()

from judge.models import Judge, Problem

def create_judge(name='judge1', auth_key='verysecretkey'):
    """Tạo judge mới"""
    try:
        judge, created = Judge.objects.get_or_create(
            name=name,
            defaults={
                'auth_key': auth_key,
                'online': True,
                'is_blocked': False
            }
        )
        if created:
            print(f"Đã tạo judge '{name}'")
        else:
            print(f"Judge '{name}' đã tồn tại")
        return judge
    except Exception as e:
        print(f"Lỗi khi tạo judge: {e}")
        return None

def assign_judge_to_problems(judge_name='judge1'):
    """Gán judge cho tất cả problems"""
    try:
        judge = Judge.objects.get(name=judge_name)
        problems = Problem.objects.all()
        count = 0
        for problem in problems:
            if judge not in problem.judges.all():
                problem.judges.add(judge)
                count += 1
        print(f"Đã gán judge '{judge_name}' cho {count} problems")
    except Judge.DoesNotExist:
        print(f"Không tìm thấy judge '{judge_name}'")
    except Exception as e:
        print(f"Lỗi khi gán judge: {e}")

def update_judge_status(judge_name='judge1', online=True, blocked=False):
    """Cập nhật trạng thái judge"""
    try:
        judge = Judge.objects.get(name=judge_name)
        judge.online = online
        judge.is_blocked = blocked
        judge.save()
        status = "online" if online else "offline"
        print(f"Đã cập nhật judge '{judge_name}' thành {status}")
    except Judge.DoesNotExist:
        print(f"Không tìm thấy judge '{judge_name}'")
    except Exception as e:
        print(f"Lỗi khi cập nhật judge: {e}")

def list_judges():
    """Liệt kê tất cả judges"""
    try:
        judges = Judge.objects.all()
        if judges:
            print("Danh sách judges:")
            for judge in judges:
                status = "online" if judge.online else "offline"
                blocked = "blocked" if judge.is_blocked else "active"
                print(f"  - {judge.name}: {status}, {blocked}")
        else:
            print("Không có judge nào")
    except Exception as e:
        print(f"Lỗi khi liệt kê judges: {e}")

def setup_judge():
    """Thiết lập judge hoàn chỉnh"""
    print("Thiết lập judge cho DMOJ...")
    
    # Tạo judge
    judge = create_judge()
    if judge:
        # Cập nhật trạng thái online
        update_judge_status()
        # Gán judge cho problems
        assign_judge_to_problems()
        print("Thiết lập judge hoàn tất!")
    else:
        print("Thiết lập judge thất bại!")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'create':
            create_judge()
        elif command == 'assign':
            assign_judge_to_problems()
        elif command == 'status':
            update_judge_status()
        elif command == 'list':
            list_judges()
        elif command == 'setup':
            setup_judge()
        else:
            print("Lệnh không hợp lệ. Sử dụng: create, assign, status, list, setup")
    else:
        setup_judge() 