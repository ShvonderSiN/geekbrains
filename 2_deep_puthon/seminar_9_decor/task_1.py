# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
from random import randint

START, STOP = 1, 5
TRIES = 5


def guess_the_number(start: int = 1, stop: int = 100, tries: int = 10) -> callable:
    """
    Загадывает число за указанное количество попыток
    Args:
        start: Начало диапазона
        stop: Конец диапазона
        tries: Число попыток

    Returns: Функция game
    """
    num = randint(start, stop + 1)

    def game() -> None:
        nonlocal tries
        while tries:
            guess = int(input('Угадайте число: '))
            if guess == num:
                print(f'Поздравляю! Вы угадали число за {tries} попытки')
                break
            else: #  ToDO доделать больше или меньше
                print('Не угадали, попробуйте еще раз')
                tries -= 1
        else:
            print('Попытки кончились')

    return game


if __name__ == '__main__':
    a = guess_the_number(START, STOP, TRIES)
    a()
