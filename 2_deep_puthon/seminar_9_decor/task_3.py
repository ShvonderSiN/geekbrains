# Задание №3
# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json
from functools import wraps


def decor(func) -> callable:
    """
    Декоратор, пишущий json
    Args:
        func: callable

    Returns:

    """
    filename = func.__name__ + '.json'

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        params = {func.__name__: {'args': args, 'kwargs': kwargs, 'result': result}}
        data.append(params)
        with open(filename, 'w+') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return func(*args, **kwargs)

    return wrapper


@decor
def task_3(a, b, c, name='Nobody', *args, **kwargs):
    return str(a + b + c) + name


if __name__ == '__main__':
    task_3(1, 2, 3, name='sergei')
    task_3(4, 5, 6, name='vasya')
    task_3(4, 5, 6, name='vasya', config=True, multy=2)
