from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import as_declarative, declared_attr

@as_declarative()
class Base:
    # 通用字段
    # 自动主键id
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # 记录创建时写入创建时间
    created_at = Column(DateTime, server_default=func.now(), comment='创建时间')
    # 记录更新时写入更新时间
    modified_at = Column(DateTime, server_default=None, onupdate=func.now(), comment='更新时间')
    #获取类名用于生成小写表名
    __name__: str

    # 自动生成表名，表名为类名的小写
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

class User(Base):
    user_name = Column(String(128), nullable=False, unique=True)
    pwd = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True, unique=True)


