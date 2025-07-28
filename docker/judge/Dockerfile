FROM dmoj/runtimes-tier1:latest

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    python3-dev python3-pip build-essential libseccomp-dev netcat-openbsd pkg-config \
    git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Tạo môi trường ảo để tránh lỗi PEP 668
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Cài đặt DMOJ judge từ PyPI thay vì từ mã nguồn
RUN pip install wheel && \
    pip install dmoj

# Tạo thư mục cho bài tập
RUN mkdir -p /problems

# Sao chép file cấu hình
COPY docker/judge/judge.yml /problems/judge.yml
COPY docker/judge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Khởi chạy
ENTRYPOINT ["/entrypoint.sh"] 