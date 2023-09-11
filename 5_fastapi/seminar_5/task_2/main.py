# Задание №2
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.
from enum import Enum
from typing import Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task 2")


class Genre(str, Enum):
    SCI_FI = "Научная фантастика"
    ROMANCE = "Романтический"
    ACTION = "Экшен"
    DRAMA = "Драма"
    COMEDY = "Комедия"


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


movies = [
    Movie(id=1, title="Плохой санта", description="Отличная комедия", genre=Genre.COMEDY),
    Movie(id=2, title="Интерстеллар", description="Отличная научная фантастика", genre=Genre.SCI_FI),
]


@app.get("/movies", response_model=List[Movie])
@app.get("/", response_model=List[Movie])
async def read_movies(gender: Optional[Genre] = None):
    if gender:
        filtered_movies = [movie for movie in movies if movie.genre == gender]
        if filtered_movies:
            return filtered_movies
        else:
            raise HTTPException(status_code=404, detail="Фильмы с данным жанром не найдены")
    elif movies:
        return movies
    raise HTTPException(status_code=404, detail="В базе фильмы отсутствуют")


@app.get("/movies/{genre}", response_model=List[Movie])
async def read_movies_by_genre(genre: Genre):
    return await read_movies(genre)
