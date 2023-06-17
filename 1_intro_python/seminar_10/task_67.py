"""
Задача №67. Решение в группах
1. Создать новый столбец в таблице с
пингвинами, который будет отвечать за
показатель длины клюва пингвина.
high - длинный(от 42)
middle - средний(от 35 до 42)
low - маленький(до 35)
"""
import seaborn as sb
import random


def task(row) -> str:
    rnd = random.randint(1, 60)
    if rnd >= 42:
        value = 'high'
    elif 35 <= rnd < 42:
        value = 'middle'
    else:
        value = 'low'
    return value


if __name__ == '__main__':
    array = sb.load_dataset('penguins')
    array['length'] = array.apply(task, axis=1)
    print(array)
