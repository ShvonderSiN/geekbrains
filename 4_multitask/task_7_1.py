# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import threading
from random import randint
from task_1 import time_decorator


@time_decorator
def compute_sum(array):
    return sum(array)


if __name__ == '__main__':
    # Создаем массив из 1 000 000 случайных целых чисел
    array = [randint(1, 100) for _ in range(1_000_000)]
    tasks = [threading.Thread(target=compute_sum, args=(array,), daemon=True) for _ in range(10)]
    for task in tasks:
        task.start()
    for task in tasks:
        task.join()
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0060 секунд
# Время выполнения функции 'compute_sum': 0.0091 секунд
# Время выполнения функции 'compute_sum': 0.0059 секунд
# Время выполнения функции 'compute_sum': 0.0090 секунд
# Время выполнения функции 'compute_sum': 0.0090 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0057 секунд
