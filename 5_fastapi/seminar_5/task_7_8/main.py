# Задание №7
# Создать RESTful API для управления списком задач. Приложение должно
# использовать FastAPI и поддерживать следующие функции:
# ○ Получение списка всех задач.
# ○ Получение информации о задаче по её ID.
# ○ Добавление новой задачи.
# ○ Обновление информации о задаче по её ID.
# ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля: ID (целое число),
# Название (строка), Описание (строка), Статус (строка): "todo", "in progress",
# "done"
from typing import List, Optional

from fastapi import FastAPI, HTTPException
from schemas import Task, Progress

app = FastAPI(title="Task 7 and 8")

tasks = [
    Task(id=1, name="Задача 1", description="Описание 1", status=Progress.todo),
    Task(id=2, name="Задача 2", description="Описание 2", status=Progress.in_progress),
    Task(id=3, name="Задача 3", description="Описание 3", status=Progress.done),
    Task(id=4, name="Задача 4", description="Описание 4", status=Progress.todo),
]


@app.get("/", response_model=List[Task])
async def get_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task_ = None
    for task in tasks:
        if task.id == task_id:
            task_ = task
    if task_ is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    return task_


@app.post("/tasks", response_model=Task)
async def create_task(task: Task, name: str, description: str, status: Progress):
    task.id = len(tasks) + 1
    new_task = Task(id=task.id, name=name, description=description, status=status)
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int,
                      new_name: Optional[str] = None,
                      new_description: Optional[str] = None,
                      new_status: Progress = Progress.todo):
    task_ = None
    for task in tasks:
        if task.id == task_id:
            task_ = task
    if task_ is None:
        raise HTTPException(status_code=404, detail="Задача не найдена")
    task_.name = new_name if new_name else task_.name
    task_.description = new_description if new_description else task_.description
    task_.status = new_status
    return task_


@app.delete("/tasks/{task_id}", response_model=str)
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return f'Задача {task.name} удалена.'
    raise HTTPException(status_code=404, detail="Задача не найдена")
