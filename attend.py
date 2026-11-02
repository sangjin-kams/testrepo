# attend.py
import datetime
import os

def show_list():
    print("\n--- 현재 출석 명단 ---")
    if os.path.exists("attendance.txt"):
        with open("attendance.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("아직 출석 기록이 없습니다.")
    print("----------------------\n")

# 1. 기존 명단 보여주기
show_list()

# 2. 새로운 출석 입력받기
name = input("이름을 입력하세요 (종료하려면 Enter): ")

if name:
    now = datetime.datetime.now()
    timestamp = now.strftime('%Y-%m-%d %H:%M:%S')

    with open("attendance.txt", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {name}님 출석\n")
    
    print(f"{name}님, 출석이 완료되었습니다!")
    
    # 3. 업데이트된 명단 다시 보여주기
    show_list()
else:
    print("입력이 없어 프로그램을 종료합니다.")