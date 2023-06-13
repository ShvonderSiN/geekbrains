"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
from random import randint


def main(coins_number: iter = 10) -> tuple:
    """
    Определяет количество монеток выпавших одно стороной
    1 - Орел
    2 - Решка
    :param coins_number: количество монеток
    """
    eagle = 0
    for coin_state in coins_number:
        if not coin_state:
            eagle += 1
        else:
            continue
    return eagle, len(coins_number) - eagle


if __name__ == '__main__':
    try:
        n = [randint(0, 1) for i in range(0, int(input('кол-во монет: ').strip()))]
        print(n)
        coins = main(n)
        print(f'Необходимо перевернуть {coins[1]} орлов либо {coins[0]} решек')
    except ValueError:
        print('Введите целое число')
