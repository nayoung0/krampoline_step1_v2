# Python 3.6 이미지를 기반으로 함
# FROM python:3.6-slim
FROM python:3.8-alpine

RUN pip install flask
RUN pip install -U Flask-Cors

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 Python 스크립트를 이미지에 추가
COPY index.py /app/

# 서버가 실행될 때 사용되는 포트
EXPOSE 8080

# 환경변수
ENV FLASK_APP=index

# 컨테이너를 시작할 때 Python 스크립트를 실행
CMD ["python", "/app/index.py"]