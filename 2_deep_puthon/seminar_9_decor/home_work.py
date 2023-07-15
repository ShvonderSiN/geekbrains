# Задание
# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import cmath

from decorator_package.decorators import save_to_json, decor_root
from decorator_package.tools import num_csv_generation


@save_to_json('home_work_num.json')
@decor_root('home_work_num.csv')
def get_sqrt(a: [int, float], b: [int, float], c: [int, float]) -> float:
    """
    Вычисляет корни квадратного уравнения
    Args:
        a: [int, float]
        b: [int, float]
        c: [int, float]
    Returns: root value
    """
    D = (b ** 2) - (4 * a * c)
    root = (-b - cmath.sqrt(D)) / (2 * a)
    return root.real


if __name__ == '__main__':
    #  генерация csv
    num_csv_generation('home_work_num.csv', 100)

    print(get_sqrt(2, 8, 3))
