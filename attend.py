# attend.py
import datetime

name = input("이름을 입력하세요: ")
now = datetime.datetime.now()

print(f"--- 출석 확인 ---")
print(f"성함: {name}")
print(f"일시: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"출석이 완료되었습니다. 오늘도 화이팅!")