from src.entity.user_entity import User
from src.view.signup import SigUpView

def main():
    signupView = SigUpView()
    while True:
        print("""
    1. 회원가입
    2. 사용자 조회
    3. 사용자 전체 조회
    4. 사용자 삭제 
    q. 프로그램 종료
    """)
        selectedMenu = input("선택 >>>")
        if selectedMenu in ("q", "Q"):
            print("프로그램을 종료합니다.")
            return

        if selectedMenu == "1":
            signupView.showSignup()
        elif selectedMenu == "2":
            pass
        elif selectedMenu == "3":
            pass
        elif selectedMenu == "4":
            pass

if __name__ == "__main__":
    main()
