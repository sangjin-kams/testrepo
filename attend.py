# attend.py
import datetime
import os

def show_list():
    print("\n========== 현재 출석 명단 ==========")
    if os.path.exists("attendance.txt"):
        with open("attendance.txt", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("기록이 없습니다.")
    print("==================================\n")

def add_attendance():
    name = input("출석할 이름을 입력하세요: ")
    if name:
        now = datetime.datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        with open("attendance.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {name}님 출석\n")
        print(f"\n✅ {name}님, 출석 체크 완료!")
    else:
        print("이름을 입력하지 않았습니다.")

# 메인 루프
while True:
    print("--- 깃허브 출석부 프로그램 ---")
    print("1. 출석하기")
    print("2. 명단보기")
    print("3. 종료하기")
    choice = input("원하는 메뉴 번호를 입력하세요: ")

    if choice == "1":
        add_attendance()
    elif choice == "2":
        show_list()
    elif choice == "3":
        print("프로그램을 종료합니다. 안녕히 가세요!")
        break
    else:
        print("잘못된 입력입니다. 다시 선택해주세요.\n")