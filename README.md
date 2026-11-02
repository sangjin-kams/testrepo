# testrepo

# 📅 GitHub 협업 출석부 프로그램

이 프로젝트는 교육장과 집을 오가며 공부하는 학습자를 위한 **GitHub 동기화 출석 관리 시스템**입니다. 
파이썬을 이용해 출석을 기록하고, 깃허브를 통해 어디서든 코드를 이어받아 개발할 수 있습니다.

## 🚀 실행 방법

### 1. 처음 시작할 때 (Clone)
```bash
git clone [본인의 저장소 주소]
cd [저장소 이름]

# 최신 코드 가져오기
git pull origin main

# 프로그램 실행
python attend.py

git add .
git commit -m "오늘의 작업 내용 기록"
git push origin main

🛠 막혔던 부분과 해결 방법 (Troubleshooting)
❓ 문제: .gitignore를 설정했는데도 attendance.txt가 자꾸 깃허브에 올라감
원인: 이미 깃허브에 한 번 커밋된 파일은 .gitignore에 등록해도 깃이 계속 추적(Tracking)하기 때문이었습니다.
해결: git rm --cached attendance.txt 명령어를 사용하여 깃의 관리 목록(캐시)에서 파일을 제거한 뒤 다시 커밋하여 해결했습니다. 이제 각자의 컴퓨터에만 출석 명단이 저장됩니다.

📚 공부 기록 (Learning Log)
📝 Git을 활용한 환경 분리
배경: 코드는 공유해야 하지만, 개인적인 출석 데이터(attendance.txt)는 공유되지 않아야 하는 상황이었습니다.
배운 점: .gitignore 파일의 역할과 이미 추적 중인 파일을 관리 목록에서 제외하는 법을 배웠습니다. 이를 통해 '공유할 코드'와 '보관할 데이터'를 분리하는 법을 익혔습니다.
적용: 메뉴 시스템을 도입하여 사용자 편의성을 높이고, 함수(def)를 사용하여 코드의 가독성을 높였습니다.
