# Задание №4
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными
# пользователей и обновлять их в базе данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
# Реализуйте валидацию данных запроса и ответа.
from typing import List
from passlib.context import CryptContext
import logging

from schemas import User
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 4")
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


@app.put("/users/{user_id}", response_model=str)
async def update_user(user_id: int, new_name: str, new_email: str, new_password: str):
    for user in users:
        if user.id == user_id:
            user.name = new_name
            user.email = new_email
            user.password = await get_password_hash(new_password)
            return f'Запись пользователя {user.name} обновлена'

    raise HTTPException(status_code=404, detail=f"Пользователь {user_id} не найден")


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"Пользователь {user_id} не найден")
