"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""
import sys


def number_sum(n) -> int:
    '''Возвращает сумму чисел n + nn + nnn'''
    try:
        return int(n) + int(n + n) + int(n + n + n)
    except ValueError:
        print('Введите целое положительное число')
        return sys.exit()


n = input('Введите число n: ')

print(number_sum(n))
