# 1. 파이썬이 설치된 가벼운 환경(이미지)을 가져옵니다.
FROM python:3.9-slim

# 2. 도커 내부의 작업 공간을 /app으로 정합니다.
WORKDIR /app

# 3. 현재 폴더의 attend.py 파일을 도커 내부(/app)로 복사합니다.
COPY attend.py .

# 4. 도커가 실행될 때 파이썬으로 attend.py를 실행하도록 설정합니다.
CMD ["python", "attend.py"]