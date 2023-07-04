from random import randint

__all__ = ['some_func', 'recon_number']

_dict_answers = {}


def recon_number(a: int, b: int, c: int) -> bool:
    """
    Игра угадай число от a до b за c попыток
    param a: Нижняя граница
    param b: Верхняя граница
    param c: Количество попыток
    """
    number = randint(a, b)
    while c > 0:
        try:
            answer = int(input('Введите число: '))
        except ValueError:
            print('Вводите только целое число!')
            continue
        if a <= answer <= b:
            if answer < number:
                print('Бери выше')
            elif answer > number:
                print('Бери ниже')
            else:
                print(f'Угадал: это число {number}')
                return True
            c -= 1
            print(f'Осталось {c} попыток')
        else:
            print(f'Вводите целое число в диапазоне: от {a} до {b}')
    else:
        return False


def puzzler(x: str, y: list, n: int) -> int:
    """
    Игра угадай число от x до y за n попыток
    param x: Нижняя граница
    param y: Верхняя граница
    param n: Количество попыток
    """
    print(x)
    good_answer = y[1]
    print('Варианты ответов:', end=' ')
    for i in range(1, len(y) + 1):
        print(f'{i}-{y[i - 1]}', end=' ')
    print()
    count = 1
    while n > 0:
        answer = input('Выберите номер ответа (1, 2, 3): ')
        if answer == '1':
            print('Не угадал')
        elif answer == '2':
            print(f'Угадал, правильный ответ {good_answer}')
            return count
        elif answer == '3':
            print('Не угадал')
        n -= 1
        count += 1
    else:
        return 0


def some_func():
    var = {'Два конца, два кольца, по-середине гвоздик': ['лыжи', 'ножницы', 'уши']}
    for i in var:
        puzzler(i, var[i], 3)
