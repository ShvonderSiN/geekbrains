"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""
import sys


def main(num) -> None:
    """
    Выводит целые степени двойки
    """
    i = 0
    while 2 ** i <= num:
        print(2 ** i)
        i += 1


if __name__ == '__main__':
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Введите целое число')
        sys.exit()
    main(number)
