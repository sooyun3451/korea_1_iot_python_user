from src.entity.user_entity import User
from src.view.signup import SigUpView
from src.repository.user_repository import UserRepository

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
            username = input("username >>> ")
            foundUser = UserRepository.findByUsername(username)
            print(foundUser if bool(foundUser) else "해당 사용자 이름의 정보가 존재하지 않습니다.")

        elif selectedMenu == "3":
            foundUsers = UserRepository.findAll()
            for user in foundUsers:
                print(user)

        elif selectedMenu == "4":
            username = input("username >>>")
            foundUser = UserRepository.findByUsername(username)
            if not bool(foundUser):
                print("해당 사용자 이름은 존재하지 않습니다.")
                continue
            password = input("password >>>")
            if foundUser.password != password:
                print("비밀번호가 일치하지 않습니다.")
                continue
            if input("사용자를 삭제하시겠습니다? (y/n)") in ('y', 'Y'):
                if UserRepository.delete(foundUser.userId) > 0:
                    print(f'삭제된 사용자 정보 >>> {foundUser}')


if __name__ == "__main__":
    main()
