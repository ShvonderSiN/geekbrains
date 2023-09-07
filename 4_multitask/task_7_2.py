# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопроцессорность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import multiprocessing
from random import randint
from task_1 import time_decorator


@time_decorator
def compute_sum(array):
    return sum(array)


if __name__ == '__main__':
    array = [randint(1, 100) for _ in range(1_000_000)]
    processes = [multiprocessing.Process(target=compute_sum, args=(array,), daemon=True) for _ in range(10)]
    for proc in processes:
        proc.start()
    for proc in processes:
        proc.join()
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0040 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0070 секунд
# Время выполнения функции 'compute_sum': 0.0040 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0060 секунд
# Время выполнения функции 'compute_sum': 0.0050 секунд
# Время выполнения функции 'compute_sum': 0.0040 секунд
