"""Задание №8
Нарисовать в консоли ёлку спросив
у пользователя количество рядов.
Пример результата:
Сколько рядов у ёлки? 5
 *
 ***
 *****
 *******
*********
"""

num_rows = int(input("Сколько рядов у ёлки? "))

for i in range(num_rows):
    for _ in range(num_rows - i - 1):
        print("", end="")

    for _ in range(2 * i + 1):
        print("*", end="")

    print()