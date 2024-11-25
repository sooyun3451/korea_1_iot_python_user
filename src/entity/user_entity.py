from dataclasses import dataclass

@dataclass
class User:
  userId: int = 0
  username:str = ''
  password: str = ''
  name: str = ''
  email: str = ''
  createDate: str = ''
  updateDate: str = ''