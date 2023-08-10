# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
from functools import wraps


def decor(func) -> callable:
    """
    Декоратор, пишущий json
    Args:
        func: callable
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        params = {func.__name__: {'args': args, 'kwargs': kwargs, 'result': result}}

        FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} {msg}'
        logging.basicConfig(level=logging.NOTSET, filename='task_3.logging.log', encoding='utf-8',
                            filemode='a', format=FORMAT, style='{', )
        logger = logging.getLogger(__name__)
        logger.info(f'Функция "{func.__name__}()" Результат выполнения: {params}')

        return func(*args, **kwargs)

    return wrapper


@decor
def task_3(a, b, c, name='Nobody', *args, **kwargs):
    return str(a + b + c) + name


if __name__ == '__main__':
    task_3(1, 2, 3, name='sergei')
    task_3(4, 5, 6, name='vasya')
    task_3(4, 5, 6, name='vasya', config=True, multy=2)
