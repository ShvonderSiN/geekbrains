"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1"""


def main(number) -> None:
    """Выводит количество элементов в массиве"""
    a = [el for el in range(1, number + 1)]
    print(a)
    x = int(input('Введите число X: '))
    final = [i for i in a if i == x]
    print(len(final))


if __name__ == '__main__':
    try:
        num = int(input('Введите количество элементов массива: '))
    except ValueError:
        print('Введите целое число')
    else:
        main(num)
