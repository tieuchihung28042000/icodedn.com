# Hướng dẫn thiết lập Judge cho DMOJ

## Vấn đề thường gặp
Khi gặp lỗi "No judge is available for this problem", hãy làm theo các bước sau:

## 🚀 Cách nhanh nhất - Script tự động hoàn chỉnh
```bash
./dmoj-site/auto_fix_judge.sh
```

Script này sẽ:
- ✅ Kiểm tra trạng thái containers
- ✅ Khởi động judge container
- ✅ Cập nhật judge online trong database
- ✅ Gán judge cho tất cả problems
- ✅ Kiểm tra kết quả

## 🔧 Cách 2: Script đơn giản
```bash
./dmoj-site/fix_judge.sh
```

## Cách 3: Thực hiện thủ công

### 1. Kiểm tra trạng thái judge
```bash
docker compose exec site python manage.py shell -c "from judge.models import Judge; j = Judge.objects.first(); print('Judge:', j.name, 'Online:', j.online, 'Blocked:', j.is_blocked)"
```

### 2. Cập nhật judge thành online
```bash
docker compose exec site python manage.py shell -c "from judge.models import Judge; j = Judge.objects.first(); j.online = True; j.save(); print('Đã cập nhật judge online')"
```

### 3. Gán judge cho problems
```bash
docker compose exec site python manage.py shell -c "from judge.models import Judge, Problem; judge = Judge.objects.first(); problems = Problem.objects.all(); [p.judges.add(judge) for p in problems]; print('Đã gán judge cho', problems.count(), 'problems')"
```

### 4. Kiểm tra kết quả
```bash
docker compose exec site python manage.py shell -c "from judge.models import Problem; p = Problem.objects.first(); print('Problem:', p.name, 'Judges:', p.judges.all())"
```

## Cấu hình Judge

### Judge Container
- **Name**: judge1
- **Auth Key**: verysecretkey
- **Bridge Address**: site:9999

### Bridge Configuration
- **Judge Address**: 0.0.0.0:9999
- **Django Address**: 0.0.0.0:9998

## Troubleshooting

### Judge không kết nối được
1. Kiểm tra logs: `docker compose logs judge`
2. Restart judge: `docker compose restart judge`
3. Kiểm tra bridge: `docker compose logs site | grep bridge`

### Judge offline
1. Cập nhật trạng thái online
2. Kiểm tra không bị blocked
3. Đảm bảo được gán cho problems

### Problems không có judge
1. Gán judge cho problems
2. Kiểm tra relationship trong database
3. Restart site container

### Judge container không chạy
1. Khởi động judge: `docker compose up -d judge`
2. Kiểm tra logs: `docker compose logs judge`
3. Chạy script tự động: `./dmoj-site/auto_fix_judge.sh`

## Lệnh hữu ích

### Liệt kê judges
```bash
docker compose exec site python manage.py shell -c "from judge.models import Judge; print('Judges:', Judge.objects.all())"
```

### Liệt kê problems
```bash
docker compose exec site python manage.py shell -c "from judge.models import Problem; print('Problems:', Problem.objects.all())"
```

### Kiểm tra judge của problem
```bash
docker compose exec site python manage.py shell -c "from judge.models import Problem; p = Problem.objects.first(); print('Problem:', p.name, 'Judges:', p.judges.all())"
```

### Kiểm tra trạng thái containers
```bash
docker compose ps
```

### Restart toàn bộ hệ thống
```bash
docker compose restart
```

## ⚡ Scripts có sẵn

1. **`auto_fix_judge.sh`** - Script tự động hoàn chỉnh (khuyến nghị)
2. **`fix_judge.sh`** - Script đơn giản
3. **`manage_judge.py`** - Script Python quản lý judge
4. **`update_judge_status.py`** - Script cập nhật trạng thái judge 