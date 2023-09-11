# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.
from typing import Optional, List, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

app = FastAPI(title='Task 1')
logger = logging.getLogger(__name__)
ERROR_404 = HTTPException(status_code=404, detail="Задача не найдена")

tasks = {}


class Task(BaseModel):
    id: int = 1 if not tasks else max(tasks.keys()) + 1
    title: str
    description: Optional[str] = None
    status: Optional[bool] = True


@app.get("/", response_model=List[Task])
@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    logger.info('Отработал GET запрос.')
    if len(tasks) == 0:
        raise ERROR_404
    return list(tasks.values())


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    logger.info('Отработал POST запрос.')
    if task.id in tasks:
        raise ERROR_404
    tasks[task.id] = task
    return task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    logger.info(f'Отработал PUT запрос для item id = {task_id = }.')
    if task_id in tasks:
        tasks[task_id].title = task.title
        tasks[task_id].description = task.description
        tasks[task_id].status = task.status
        return tasks[task_id]
    raise ERROR_404


@app.delete("/tasks/{task_id}", response_model=str)
async def delete_task(task_id: int):
    logger.info('Отработал DELETE запрос.')
    if task_id in tasks:
        deleted_task = tasks.pop(task_id)
        return f'Задача {deleted_task} удалена.'
    raise ERROR_404
