from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from model.base import Base
from core_settiing import setting

class DBService:
    #从.env中读取数据库配置信息
    REMOTE_DATABASE_URL = setting.REMOTE_DATABASE_URL
    #本地测试数据库
    LOCAL_DATABASE_URL = setting.LOCAL_DATABASE_URL
    DEV_DATABASE = 'test_db'
    db_url = LOCAL_DATABASE_URL+DEV_DATABASE
    #创建表
    engine = create_engine(db_url, echo=True)
    #创建会话
    SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db(self) -> Generator[Session, None, None]:
        db = self.SessionFactory()
        try:
            yield db
        finally:
            db.close()

    def init_db(self) -> None:
        Base.metadata.create_all(bind=self.engine)


db_servie = DBService()

# if __name__ == '__main__':
