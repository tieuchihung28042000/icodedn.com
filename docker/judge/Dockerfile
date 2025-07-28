FROM dmoj/runtimes-tier3:latest

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    python3-dev python3-pip build-essential libseccomp-dev netcat-openbsd \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Cài đặt DMOJ judge
COPY dmoj-judge/ /judge/
WORKDIR /judge
RUN pip3 install -e .

# Tạo thư mục cho bài tập
RUN mkdir -p /problems

# Sao chép file cấu hình
COPY docker/judge/judge.yml /problems/judge.yml
COPY docker/judge/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Khởi chạy
ENTRYPOINT ["/entrypoint.sh"] 