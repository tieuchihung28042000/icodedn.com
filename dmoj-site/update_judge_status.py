#!/usr/bin/env python
"""
Script để cập nhật trạng thái judge trong DMOJ
"""
import os
import sys
import django

# Thêm đường dẫn project vào sys.path
sys.path.append('/app')

# Thiết lập Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dmoj.settings')
django.setup()

from judge.models import Judge

def update_judge_status():
    """Cập nhật trạng thái judge thành online"""
    try:
        # Lấy judge đầu tiên
        judge = Judge.objects.first()
        if judge:
            judge.online = True
            judge.is_blocked = False
            judge.save()
            print(f"Đã cập nhật judge '{judge.name}' thành online")
        else:
            print("Không tìm thấy judge nào")
    except Exception as e:
        print(f"Lỗi khi cập nhật judge: {e}")

if __name__ == '__main__':
    update_judge_status() 