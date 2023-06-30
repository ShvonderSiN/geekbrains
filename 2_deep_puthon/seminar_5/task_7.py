# Задание №7
# ✔ Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».
import sys


def is_simple(n) -> bool:
    """Проверяет, простое ли число"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


def simple_gen(num: int) -> iter:
    if num == 0:
        raise ValueError('Ожидается положительное число')

    count = 1
    for i in range(sys.maxsize):
        if is_simple(i):
            count += 1
            yield i
        if count > abs(num):
            break


print(*simple_gen(0))
# Видел в интернете решения где корнем проверяется, там более оптимально
# я как от математики далекий, там и не смог понять как это ускоряет расчет)))
# for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             is_prime = False
#             break
# решил сделать так как сделал