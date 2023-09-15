import datetime
import decimal
from enum import Enum

from pydantic import BaseModel, Field, EmailStr


class Status(Enum):
    IN_PROGRESS = 0
    DONE = 1


class OrderInSchema(BaseModel):
    """Схема заказа без id"""
    date: datetime.datetime
    status: Status = Status.IN_PROGRESS


class OrderSchema(OrderInSchema):
    """Схема заказа с id"""
    id: int
    good_id: int
    user_id: int


class GoodInSchema(BaseModel):
    """Схема товара без id"""
    title: str = Field(..., min_length=2)
    description: str = Field(default=None, min_length=2)
    price: decimal.Decimal


class GoodSchema(GoodInSchema):
    """Схема товара с id"""
    id: int


class UserInSchema(BaseModel):
    """Схема пользователя без id"""
    name: str = Field(..., min_length=2)
    surname: str = Field(..., min_length=2)
    email = EmailStr
    password = str


class UserSchema(UserInSchema):
    """Схема пользователя с id"""
    id: int
