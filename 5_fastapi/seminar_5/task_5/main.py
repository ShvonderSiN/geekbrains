# Задание №5
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и
# удалять информацию о пользователе из базы данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).
# Реализуйте проверку наличия пользователя в списке и удаление его из
# списка.

from typing import List
from passlib.context import CryptContext
import logging

from schemas import User
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Task 5")
logger = logging.getLogger(__name__)

users = [
    User(id=1, name="Вася", email="vasya@yandex.com", password="password123"),
    User(id=2, name="Петя", email="petya@ya.com", password="password456"),
]


@app.get("/users", response_model=List[User])
async def read_users():
    return users


@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail=f"Пользователь {user_id} не найден")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return f'Пользователь {user.name} удален'
    raise HTTPException(status_code=404, detail=f"Пользователь {user_id} не найден")
