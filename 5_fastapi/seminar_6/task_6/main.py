descr = """Задание №6
Необходимо создать базу данных для интернет-магазина. База данных должна
состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
содержать информацию о доступных товарах, их описаниях и ценах. Таблица
пользователи должна содержать информацию о зарегистрированных
пользователях магазина. Таблица заказы должна содержать информацию о
заказах, сделанных пользователями.
○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
имя, фамилия, адрес электронной почты и пароль.
○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
название, описание и цена.
○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
заказа.
Создайте модели pydantic для получения новых данных и
возврата существующих в БД для каждой из трёх таблиц
(итого шесть моделей).
Реализуйте CRUD операции для каждой из таблиц через
создание маршрутов, REST API (итого 15 маршрутов).
○ Чтение всех
○ Чтение одного
○ Запись
○ Изменение
○ Удаление"""
from typing import List
from fastapi import FastAPI, HTTPException
from sqlalchemy import select, delete, insert, update

from models import UserModel, OrderModel, GoodModel
from schemas import *
from database import startup, shutdown, db
from tools import get_password_hash

app = FastAPI(title='Seminar_6, Task 6', description=descr)
app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)


@app.get("/users/", response_model=List[UserSchema])
async def get_all_users() -> List[UserSchema]:
    """Чтение всех пользователей"""
    query = select(UserModel)
    users = await db.fetch_all(query)

    if users:
        return users

    raise HTTPException(status_code=404, detail="Нет ни одного пользователя")


@app.get('/orders/', response_model=List[OrderSchema])
async def get_all_orders() -> List[OrderSchema]:
    """Чтение всех заказов"""
    query = select(OrderModel)
    orders = await db.fetch_all(query)

    if orders:
        return orders

    raise HTTPException(status_code=404, detail="Нет ни одного заказа")


@app.get('/goods/', response_model=List[GoodSchema])
async def get_all_goods() -> List[GoodSchema]:
    """Чтение всех товаров"""
    query = select(GoodModel)
    goods = await db.fetch_all(query)

    if goods:
        return goods

    raise HTTPException(status_code=404, detail="Нет ни одного товара")


@app.get('/users/{user_id}', response_model=UserSchema)
async def get_single_user(user_id: int) -> UserSchema:
    """Чтение одного пользователя по id"""
    query = select(UserModel).where(UserModel.id == user_id)
    db_user = await db.fetch_one(query)

    if db_user:
        return db_user

    raise HTTPException(status_code=404, detail="Пользователь не найден")


@app.get('/orders/{order_id}', response_model=OrderSchema)
async def get_single_order(order_id: int) -> OrderSchema:
    """Чтение одного заказа по id"""
    query = select(OrderModel).where(OrderModel.id == order_id)
    db_order = await db.fetch_one(query)

    if db_order:
        return db_order

    raise HTTPException(status_code=404, detail="Заказ не найден")


@app.get('/goods/{good_id}', response_model=GoodSchema)
async def get_single_good(good_id: int) -> GoodSchema:
    """Чтение одного товара по id"""
    query = select(GoodModel).where(GoodModel.id == good_id)
    db_good = await db.fetch_one(query)

    if db_good:
        return db_good

    raise HTTPException(status_code=404, detail="Товар не найден")


@app.post('/users/', response_model=UserSchema)
async def create_user(user: UserInSchema) -> dict:
    """Создание нового пользователя"""
    hashed_password = await get_password_hash(str(user.password))
    user_dict = user.dict()
    user_dict['password'] = hashed_password
    query = insert(UserModel).values(**user_dict)
    new_user_id = await db.execute(query, user_dict)
    return {**user_dict, 'id': new_user_id}


from schemas import OrderInSchema, GoodInSchema  # убедитесь, что вы импортировали эти схемы


@app.post('/orders/', response_model=OrderSchema)
async def create_order(order: OrderInSchema) -> dict:
    """Создание нового заказа"""
    query = insert(OrderModel).values(**order.dict())
    new_order_id = await db.execute(query, order.dict())
    return {**order.dict(), 'id': new_order_id}


@app.post('/goods/', response_model=GoodSchema)
async def create_good(good: GoodInSchema) -> dict:
    """Создание нового товара"""
    query = insert(GoodModel).values(**good.dict())
    new_good_id = await db.execute(query, good.dict())
    return {**good.dict(), 'id': new_good_id}


@app.put('/users/{user_id}', response_model=UserSchema)
async def update_user(user_id: int, user: UserInSchema) -> dict:
    """Обновление данных пользователя"""
    query = select(UserModel).where(UserModel.id == user_id)
    db_user = await db.fetch_one(query)

    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user_dict = user.dict()
    user_dict['password'] = await get_password_hash(str(user.password))
    query = update(UserModel).where(UserModel.id == user_id).values(**user_dict)
    await db.execute(query)

    return {**user_dict, 'id': user_id}


@app.put('/orders/{order_id}', response_model=OrderSchema)
async def update_order(order_id: int, order: OrderInSchema) -> dict:
    """Обновление данных заказа"""
    query = select(OrderModel).where(OrderModel.id == order_id)
    db_user = await db.fetch_one(query)

    if not db_user:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    query = update(OrderModel).where(OrderModel.id == order_id).values(**order.dict())
    await db.execute(query)

    return {**order.dict(), 'id': order_id}


@app.put('/goods/{good_id}', response_model=GoodSchema)
async def update_good(good_id: int, good: GoodInSchema) -> dict:
    """Обновление данных товара"""
    query = select(GoodModel).where(GoodModel.id == good_id)
    db_user = await db.fetch_one(query)

    if not db_user:
        raise HTTPException(status_code=404, detail="Товар не найден")

    query = update(GoodModel).where(GoodModel.id == good_id).values(**good.dict())
    await db.execute(query)

    return {**good.dict(), 'id': good_id}


@app.delete('/users/{user_id}', response_model=UserSchema)
async def delete_user(user_id: int) -> UserSchema:
    """Удаление пользователя по id"""
    query = select(UserModel).where(UserModel.id == user_id)
    db_user = await db.fetch_one(query)

    if not db_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    query = delete(UserModel).where(UserModel.id == user_id)
    await db.execute(query)

    return db_user


@app.delete('/orders/{order_id}', response_model=OrderSchema)
async def delete_order(order_id: int) -> OrderSchema:
    """Удаление заказа по id"""
    query = select(OrderModel).where(OrderModel.id == order_id)
    db_order = await db.fetch_one(query)

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    query = delete(OrderModel).where(OrderModel.id == order_id)
    await db.execute(query)

    return db_order


@app.delete('/goods/{good_id}', response_model=GoodSchema)
async def delete_good(good_id: int) -> GoodSchema:
    """Удаление товара по id"""
    query = select(GoodModel).where(GoodModel.id == good_id)
    db_good = await db.fetch_one(query)

    if not db_good:
        raise HTTPException(status_code=404, detail="Товар не найден")

    query = delete(GoodModel).where(GoodModel.id == good_id)
    await db.execute(query)

    return db_good


if __name__ == '__main__':
    import asyncio

    asyncio.run(startup())


    async def virgin_db():
        # query = delete(UserModel)
        # await db.execute(query)
        query = insert(OrderModel)

        for i in range(2):
            user_id = i
            good_id = i
            date = datetime.now()
            new_order = {"user_id": user_id, "good_id": good_id, "date": date, "status": Status.IN_PROGRESS}
            await db.execute(query, new_order)


    asyncio.run(virgin_db())
