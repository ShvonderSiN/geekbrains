from random import sample

__all__ = ['num_csv_generation']
_START = 1
_STOP = 100


def num_csv_generation(dest: str, rows: int):
    """
    Генерирует csv файл с тремя
    случайными числами в каждой строке
    Args:
        dest: Имя сохраняемого файла
        rows: Количество строк для генерации
    """
    range_ = range(_START, _STOP + 1)
    with open(dest, 'w') as f:
        for _ in range_:
            num_1, num_2, num_3 = sample(range_, rows)
            f.write(f'{num_1},{num_2},{num_3}\n')
