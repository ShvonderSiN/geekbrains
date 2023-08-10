# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

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

        logging.basicConfig(level=logging.NOTSET, filename='task_2.logging.log', encoding='utf-8',
                            filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', )
        logger = logging.getLogger(__name__)
        logger.info(f'Результат выполнения: {params}')

        return func(*args, **kwargs)

    return wrapper


@decor
def task_3(a, b, c, name='Nobody', *args, **kwargs):
    return str(a + b + c) + name


if __name__ == '__main__':
    task_3(1, 2, 3, name='sergei')
    task_3(4, 5, 6, name='vasya')
    task_3(4, 5, 6, name='vasya', config=True, multy=2)
