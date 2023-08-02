"""Задание
✔ Решить задачи, которые не успели решить на семинаре.
"""

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRIALS = 10


def guessing() -> None:
    """
    ✔ Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
    """
    num = randint(LOWER_LIMIT, UPPER_LIMIT + 1)
    count = TRIALS

    while TRIALS > 0:
        try:
            ges_num = float(input('Введи число: '))
        except ValueError:
            print('Принимаются только цифры')
            continue

        if ges_num > num:
            print('Бери ниже')
        elif ges_num < num:
            print('Бери выше')
        elif ges_num == num:
            print('Угадал!')
            break
        count -= 1
        print(f'Осталось {count} попыток')
    else:
        print('Попытки кончились')


def task_triangle() -> None:
    """
    ✔ Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.
    """
    a = float(input("Сторона А: "))
    b = float(input("Сторона Б: "))
    c = float(input("Сторона C: "))

    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")

        if a == b and b == c:
            print("Треугольник равносторонний")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник не существует")


def check_number() -> None:
    """
    ✔ Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
    """
    while True:
        number = int(input('Enter the number: '))
        if not 0 < number < 100000:
            continue
        if number % 1 == 0 and number % number == 0 and not number % 2 == 0:
            print(f'{number} простое число')
        else:
            print(f'{number} составное число')
        break


if '__main__' == __name__:
    from random import randint

    task_triangle()
    check_number()
    guessing()
