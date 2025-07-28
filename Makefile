.PHONY: build up down restart logs shell-site shell-judge clean

# Biên dịch tất cả các container
build:
	docker compose build

# Khởi động tất cả các container
up:
	docker compose up -d

# Dừng tất cả các container
down:
	docker compose down

# Khởi động lại tất cả các container
restart:
	docker compose restart

# Xem logs của tất cả các container
logs:
	docker compose logs -f

# Xem logs của một container cụ thể
logs-%:
	docker compose logs -f $*

# Truy cập shell của site container
shell-site:
	docker compose exec site bash

# Truy cập shell của judge container
shell-judge:
	docker compose exec judge bash

# Xóa tất cả các container và volume
clean:
	docker compose down -v

# Tạo superuser mới
create-superuser:
	docker compose exec site python manage.py createsuperuser

# Tạo bài tập demo
load-demo:
	docker compose exec site python manage.py loaddata demo

# Tạo ngôn ngữ
load-languages:
	docker compose exec site python manage.py loaddata language_all

# Backup database
backup-db:
	docker compose exec db mysqldump -u dmoj -pdmojpass dmoj > backup.sql

# Khôi phục database
restore-db:
	docker compose exec -T db mysql -u dmoj -pdmojpass dmoj < backup.sql 