from src.entity.user_entity import User
from src.repository.user_repository import UserRepository


class SigUpView:

    def showSignup(self):
        username = self.getUsernameInputValue()
        password = self.getInputValue("비밀번호", "password")
        name = self.getInputValue("성명", "name")
        email = self.getInputValue("이메일", "email")

        signupUser = User(username=username, password=password, name=name, email=email)
        UserRepository.saveUser(signupUser)

        if signupUser.userId == 0:
            print("회원가입 실패!!")
            return

        print(f"{signupUser.username} 회원가입 완료!! userId={signupUser.username}")

    def isEmpty(self, value: str = ""):
        return len(value.strip()) == 0

    def getUsernameInputValue(self):
        while True:
            username = input("username >>> ")
            if not self.isEmpty(username):
                foundUser = UserRepository.findByUsername(username)
                if not bool(foundUser):
                    return username
                print("해당 사용자 이름은 이미 사용중입니다.")
                continue
            print("사용자 이름은 공백일 수 없습니다.")


    def getInputValue(self, label: str, message: str):
        while True:
            value = input(f"{message} >>> ")
            if not self.isEmpty(value):
                return value
            print(f"{label}은(는) 공백일 수 없습니다.")

