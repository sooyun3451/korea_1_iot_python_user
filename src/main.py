from src.entity.user_entity import User
from src.repository.user_repository import UserRepositoryStudy

def main():
  newUser = User(username='ddd', password='ddd123', name='홍길북', email='ddd@gmail.com')
  userRepository = UserRepositoryStudy()
  userRepository.insert(newUser)
  userRepository.findById(4)

if __name__ == "__main__": 
  main()