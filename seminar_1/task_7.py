"""Задание №7
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
"""


def get_square(x) -> int:
    """Возвращает квадрат числа"""
    return int(x) ** 2


def get_product(x, y) -> int:
    """Возвращает произведение двух чисел"""
    return int(x) * int(y)


def get_reverse(x: str) -> str:
    """Возвращает зеркальное отображение числа"""
    return x[::-1]


if '__main__' == __name__:
    while True:
        num = input('Введите число от 1 до 999: ')
        length = len(num)

        try:
            if 1 <= int(num) <= 999:
                if length == 1:
                    res = get_square(num)
                elif length == 2:
                    res = get_product(num[0], num[1])
                else:
                    res = get_reverse(num)
                print(res)
                break
            else:
                continue
        except ValueError:
            # print('Пожалуйста, введите целое число от 1 до 999')
            continue