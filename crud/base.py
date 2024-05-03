import os, sys
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from model.base import Base
import faker

class DBService:
    #从.env中读取数据库配置信息
    REMOTE_DATABASE_URL = os.getenv('REMOTE_DATABASE_URL')
    #本地测试数据库
    LOCAL_DATABASE_URL = 'mysql+pymysql://root:140323@localhost:3306/'
    DEV_DATABASE = 'test_db'
    #创建表
    engine = create_engine(LOCAL_DATABASE_URL+DEV_DATABASE, echo=True)
    #创建会话
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db(self) -> Generator[Session, None, None]:
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    def init_db(self) -> None:
        Base.metadata.create_all(bind=self.engine)
        session = self.SessionLocal()
        #检查user表和admin表中是否有数据，无则加入
        from model.base import User
        results = self.SessionLocal().query(User).all()
        if len(results) == 0:
            print("No users")
            users = [User(user_name='guest', email='localhost@guest.com', pwd='hello!')]
            from model.base import User
            for i in range(10):
                fake = faker.Faker()
                user_name = fake.name()
                password = fake.password(length=6)
                email = fake.email()
                user = User(user_name=user_name, pwd=password, email=email)
                users.append(user)
            print('added some')

            session.add_all(users)
            session.commit()
            session.close()



db_servie = DBService()

# if __name__ == '__main__':
