FROM python:3.10-slim

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    python3-dev python3-pip build-essential libseccomp-dev netcat-openbsd pkg-config \
    git gcc g++ make curl libcap-dev \
    openjdk-17-jdk-headless \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Tạo user không có quyền root
RUN useradd -m -s /bin/bash dmoj

# Cài đặt DMOJ judge từ PyPI
RUN pip install wheel && \
    pip install dmoj

# Tạo thư mục cho bài tập và cấp quyền
RUN mkdir -p /problems && chown dmoj:dmoj /problems

# Sao chép file cấu hình
COPY docker/judge/judge.yml /problems/judge.yml
COPY docker/judge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && chown dmoj:dmoj /problems/judge.yml

# Chuyển sang user dmoj
USER dmoj

# Khởi chạy
ENTRYPOINT ["/entrypoint.sh"] 