# Задание №6
# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.
from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from passlib.context import CryptContext

from schemas import User

app = FastAPI(title="Task 6")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

users = [
    User(id=1, name="Вася", email="vasya@yandex.com", password="password123"),
    User(id=2, name="Петя", email="petya@ya.com", password="password456"),
]


def menu_html():
    menu = {
        "Home": "/",
        "Add user": "/add_user"
    }
    return menu


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, menu: dict = Depends(menu_html)):
    all_users = users
    return templates.TemplateResponse("index.html", {"request": request, "users": all_users, "menu": menu})


async def hash_password(password):
    return pwd_context.hash(password)


@app.get("/add_user", response_class=HTMLResponse)
@app.post("/add_user", response_class=HTMLResponse)
async def create_user(request: Request,
                      name: str = Form(default=None, min_length=3, max_length=50, regex="^[а-яА-Яa-zA-Z]+$"),
                      email: str = Form(default=None, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"),
                      password: str = Form(default=None, min_length=8),
                      menu: dict = Depends(menu_html)):
    if request.method == "POST":
        new_id = len(users) + 1
        new_user = User(id=new_id, name=name, email=email, password=await hash_password(password))
        users.append(new_user)
        return RedirectResponse("/", status_code=303)
    return templates.TemplateResponse("add_user.html", {"request": request, "menu": menu})
