from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, func, Float, ForeignKey, Enum as SQLAlchemyEnum
from sqlalchemy.orm import as_declarative, declared_attr, validates
from sqlalchemy.inspection import inspect
from enum import Enum

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

    def to_dict(self) -> dict: # model转换字典，主要未来避免InstanceState字段出现
        return {
            c.key: getattr(self, c.key).isoformat() if isinstance(getattr(self, c.key), datetime)
            else getattr(self,c.key) for c in inspect(self).mapper.column_attrs # 对于时间字段，需要转换成字符串因为时间字段不可序列化
        }

class User(Base):
    user_name = Column(String(128), nullable=False, unique=True)
    pwd = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True, unique=True)
    last_login = Column(DateTime, server_default=func.now(), nullable=False)

class Category(Base):
    category_name = Column(String(128), nullable=False, unique=True)
class Product(Base):
    product_name = Column(String(128), nullable=False, unique=True)
    price = Column(Float, nullable=False, )
    quantity = Column(Integer, nullable=False, default=0)
    description = Column(String(128), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    @validates('price')
    def validate_price(self, key, value):
        if not isinstance(value, float) or value < 0:
            raise ValueError('price must be positive')
        return value
    @validates('quantity')
    def validate_quantity(self, key, value):
        if not isinstance(value, float) or value <= 0:
            raise ValueError('quantity must be positive')
        return value

class OrderStatus(Enum):
    PAID = 'paid'
    REFUND = 'refund'
    DELIVERED = 'delivered'
    RECEIVED = 'received'

class Order(Base):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    status = Column(SQLAlchemyEnum(OrderStatus))

class OrderItem(Base):
    __tablename__ = 'order_item'
    order_id = Column(Integer, ForeignKey('order.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)

class Cart(Base):
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    status = Column(SQLAlchemyEnum(OrderStatus))

class CartItem(Base):
    __tablename__ = 'cart_item'
    cart_id = Column(Integer, ForeignKey('cart.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
    price_at_time = Column(Float, nullable=False)


if __name__ == '__main__':
    print(User().to_dict())
