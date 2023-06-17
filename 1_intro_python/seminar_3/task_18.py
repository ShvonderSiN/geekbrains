"""Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5"""


def main(arr, x) -> None:
    """Выводит самый близкий по величине элемент к заданному числу X в массиве"""
    closest_element = None
    min_difference = float('inf')

    for num in arr:
        difference = abs(num - x)
        if difference < min_difference:
            min_difference = difference
            closest_element = num

    return closest_element


if __name__ == '__main__':
    try:
        array = list(map(int, input('Введите количество элементов массива: ').split()))
        x = int(input('Введите число X: '))
    except ValueError:
        print('Введите целое число')
    else:
        print(main(arr=array, x=x))
