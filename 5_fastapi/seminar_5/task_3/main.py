# Задание №3
# Создать API для добавления нового пользователя в базу данных. Приложение
# должно иметь возможность принимать POST запросы с данными нового
# пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.

from typing import List
from passlib.context import CryptContext
import logging

from schemas import User
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 3")
logger = logging.getLogger(__name__)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = [
    User(id=1, name="Вася", email="vasya@yandex.com", password="password123"),
    User(id=2, name="Петя", email="petya@ya.com", password="password456"),
]


@app.get("/users", response_model=List[User])
async def read_users():
    return users


async def get_password_hash(password: str):
    return pwd_context.hash(password)


@app.post("/users", response_model=User)
async def create_user(name: str, email: str, password: str):
    hashed_password = await get_password_hash(password)
    new_user = User(id=len(users) + 1, name=name, email=email, password=hashed_password)
    users.append(new_user)
    return new_user


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"Пользователь {user_id} не найден")
