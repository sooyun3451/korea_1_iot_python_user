from pymysql import cursors
from dataclasses import dataclass

from src.config.database_config import DatabaseConfig
from src.entity.user_entity import User

@dataclass
class UserRepositoryStudy:

  def insert(self, user: User):
    connection = DatabaseConfig.getConnection()
    cursor = connection.cursor()
    sql = '''
    insert into user_tb
    values(default, %s, %s, %s, %s, now(), now())
    '''
    insertCount = cursor.execute(query=sql, args=(user.username, user.password, user.name, user.email))
    print(f'User데이터 추가 성공 {insertCount}건')
    connection.commit()


  def findById(self, user_id: int):
    connection = DatabaseConfig.getConnection()
    cursor = connection.cursor(cursor=cursors.DictCursor)
    sql = '''
    select * from user_tb where user_id = %s
    '''
    cursor.execute(query=sql, args=(user_id,))
    result = cursor.fetchone()
    print(result)