# attend.py
import datetime

name = input("이름을 입력하세요: ")
now = datetime.datetime.now()
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

# attendance.txt 파일에 이름과 시간을 저장하는 기능 추가
with open("attendance.txt", "a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] {name}님 출석\n")

print(f"--- 출석 완료 ---")
print(f"{name}님의 출석 기록이 attendance.txt에 저장되었습니다.")