from tkinter.constants import E

from pymysql import cursors, connect
from dataclasses import dataclass

from src.config.database_config import DatabaseConfig
from src.entity.user_entity import User

class UserRepository:

  @staticmethod
  def findByUsername(username: str):
    foundUser = None

    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor(cursor=cursors.DictCursor)
        sql = "select * from user_tb where username = %s"
        cursor.execute(query=sql, args=(username, ))
        result = cursor.fetchone()
        if bool(result):
          foundUser = User(
            userId=result['user_id'],
            username=result['username'],
            password=result['password'],
            name=result['name'],
            email=result['email'],
            createDate=result['create_date'],
            updateDate=result['update_date']
          )
      except Exception as e:
        print(e)
      finally:
        connection.close()
    except Exception as e:
      print(e)
      print("데이터베이스 연결 실패")

    return foundUser

  @staticmethod
  def saveUser(user: User):
    connection = None
    try:
      connection = DatabaseConfig.getConnection()
      try:
        cursor = connection.cursor()
        sql = '''
          insert into user_tb values(default, %s, %s, %s, %s, now(), now())
        '''
        cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
        user.userId = cursor.lastrowid
        # lastrowid: 마지막 로우의 id, 마지막에 들어간 데이터의 PK 값
        connection.commit()
      except Exception as e:
        print(e)
        print("사용자 정보 추가 실패!!!")
      finally:
        connection.close()
    except Exception as e:
      print(e)