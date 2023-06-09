"""
Задача 26: Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""


def grade(a, b) -> int:
    """Функция возведения числа в степень,
    только для положительных степеней

    Args:
        a (int): число, возводимое в степень
        b (int): степень
    """
    if b < 1 or b == 0:
        return 1
    return a * grade(a=a, b=b - 1)

if __name__ == '__main__':
    print(grade(3, 5))
