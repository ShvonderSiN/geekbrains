# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.

import asyncio
from random import randint


def time_decorator(func):
    async def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        result = await func(*args, **kwargs)
        print(f'Время выполнения: {time.time() - start_time:.2f} sec')
        return result

    return wrapper


@time_decorator
async def compute_sum(array):
    s = sum(array)
    print("Сумма элементов массива:", s)
    return s


async def main(array):
    tasks = [asyncio.create_task(compute_sum(array)) for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    array = [randint(1, 100) for _ in range(1000000)]
    asyncio.run(main(array))
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
# Сумма элементов массива: 50493608
# Время выполнения: 0.01 sec
