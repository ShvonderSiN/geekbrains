"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""


def amount(a, b) -> int:
    """
    Сложение двух положительных чисел с помощью рекурсии
    Args:
        a (int): положительное число
        b (int): положительное число
    """
    if a < 0 or b < 0:
        raise ValueError("Оба числа должны быть положительными")
    elif a == 0:
        return b
    return amount(a - 1, b + 1)


if __name__ == '__main__':
    print(amount(2, 2))
    print(amount(23, 17))
    print(amount(22, 31))