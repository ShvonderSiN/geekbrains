# Задание №2
# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.

from functools import wraps
from random import randint, randrange, sample, choice

START, STOP = 1, 100
TRIES = 10


def guess_the_number(func) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):

        if False in (START <= args[0] < STOP,
                     START < args[1] <= STOP,
                     args[2] in range(1, TRIES + 1)):
            args = *sorted(sample(range(START, STOP + 1), 2)), choice(range(1, TRIES + 1))
            res = func(*args, **kwargs)

        else:
            res = func(*args, **kwargs)

        return res

    return wrapper


@guess_the_number
def game(start: int = 1, stop: int = 100, tries: int = 10) -> None:
    """
    Загадывает число за указанное количество попыток
    Args:
        start: Начало диапазона
        stop: Конец диапазона
        tries: Число попыток
    Returns: None
    """
    num = randint(start, stop)
    while tries:
        guess = int(input('Угадайте число: '))
        if guess == num:
            print(f'Поздравляю! Вы угадали число за {tries} попытки')
            break
        else:
            print('Не угадали, попробуйте еще раз')
            tries -= 1
    else:
        print('Попытки кончились')


if __name__ == '__main__':
    game(1, 5, 15)
    print(game.__name__)
    help(game)
