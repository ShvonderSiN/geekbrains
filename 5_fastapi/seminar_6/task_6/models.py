from sqlalchemy import Column, Integer, String, Enum, DECIMAL, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from schemas import Status

Base = declarative_base()


class UserModel(Base):
    """Таблица Users"""
    __tablename__ = 'users_task_6'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String(length=50))
    surname = Column(String(length=50))
    email = Column(String(length=100), unique=True, index=True)
    password = Column(String, nullable=False)
    orders = relationship('OrderModel', backref='user')

    def __str__(self):
        return f'{self.surname} {self.name}'

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, surname={self.surname})'


class GoodModel(Base):
    """Таблица товаров"""
    __tablename__ = 'goods_task_6'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String(length=50))
    description = Column(String(length=250), index=True)
    price = Column(DECIMAL(10, 2), nullable=False)
    orders = relationship('OrderModel', backref='good')

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Good(id={self.id}, name={self.title})'


class OrderModel(Base):
    """Таблица заказов"""
    __tablename__ = 'orders_task_6'
    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    user_id = Column(ForeignKey('users_task_6.id'), nullable=False)
    good_id = Column(ForeignKey('goods_task_6.id'), nullable=False)
    date = Column(DateTime, nullable=False)
    status = Column(Enum(Status), default=Status.IN_PROGRESS, nullable=False)

    def __str__(self):
        return f'Заказ {self.id}'

    def __repr__(self):
        return f'Order(id={self.id}, user_id={self.user_id}, good_id={self.good_id})'
