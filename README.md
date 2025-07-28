# DMOJ - Docker All-in-One

Đây là bản đóng gói Docker cho hệ thống DMOJ (Online Judge) bao gồm tất cả các thành phần cần thiết.

## Thành phần

- **DMOJ Site**: Giao diện web và backend Django
- **DMOJ Judge**: Hệ thống chấm bài với hỗ trợ nhiều ngôn ngữ lập trình
- **MariaDB**: Cơ sở dữ liệu
- **Redis**: Cache và message broker cho Celery

## Yêu cầu

- Docker và Docker Compose
- Ít nhất 4GB RAM
- Ít nhất 20GB dung lượng ổ đĩa

## Cài đặt

1. Clone repository:
   ```
   git clone https://github.com/yourusername/dmoj-docker.git
   cd dmoj-docker
   ```

2. Tạo thư mục cho bài tập:
   ```
   mkdir -p problems
   ```

3. Khởi động các container:
   ```
   docker-compose up -d
   ```

4. Truy cập trang web:
   ```
   http://localhost:8000
   ```

## Tài khoản mặc định

- **Username**: admin
- **Password**: admin

## Cấu hình

### Thêm Judge

1. Đăng nhập vào trang quản trị: http://localhost:8000/admin
2. Vào phần Judges > Judges > Add Judge
3. Nhập tên judge và key (mặc định là "judge1" và "verysecretkey")
4. Lưu lại

### Thêm bài tập

Thêm bài tập vào thư mục `problems/` theo định dạng DMOJ. Mỗi bài tập nên có cấu trúc như sau:

```
problems/
  problem-code/
    init.yml
    problem.md (hoặc problem.tex)
    test_cases/
      input.1
      output.1
      ...
```

## Các biến môi trường

### Site

- `MYSQL_HOST`: Host của MariaDB (mặc định: db)
- `MYSQL_DATABASE`: Tên database (mặc định: dmoj)
- `MYSQL_USER`: Tên người dùng database (mặc định: dmoj)
- `MYSQL_PASSWORD`: Mật khẩu database (mặc định: dmojpass)
- `REDIS_HOST`: Host của Redis (mặc định: redis)
- `DEBUG`: Chế độ debug (mặc định: False)

### Judge

- `JUDGE_NAME`: Tên của judge (mặc định: judge1)
- `JUDGE_KEY`: Key xác thực của judge (mặc định: verysecretkey)
- `BRIDGE_ADDRESS`: Địa chỉ của bridge (mặc định: site)
- `BRIDGE_PORT`: Cổng của bridge (mặc định: 9999)

## Backup và khôi phục

### Backup database

```
docker exec -it dmoj-db mysqldump -u dmoj -pdmojpass dmoj > backup.sql
```

### Khôi phục database

```
docker exec -i dmoj-db mysql -u dmoj -pdmojpass dmoj < backup.sql
```

## Cập nhật

1. Pull các thay đổi mới:
   ```
   git pull
   ```

2. Rebuild và khởi động lại các container:
   ```
   docker-compose down
   docker-compose build
   docker-compose up -d
   ```

## Gỡ lỗi

### Xem logs

```
docker-compose logs -f site
docker-compose logs -f judge
docker-compose logs -f bridged
docker-compose logs -f celery
```

### Truy cập shell

```
docker-compose exec site bash
docker-compose exec judge bash
``` 