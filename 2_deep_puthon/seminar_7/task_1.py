# Задание №1
# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции


def gen(file_name: str = 'file.txt', count: int = 10) -> None:
    """функция, которая заполняет файл"""
    for _ in range(count):
        rand_int, rand_float = randint(-1000, 1000), round(uniform(-1000, 1000), 2)
        data = f'{rand_int}/{rand_float}\n'
        writer(file_name, data=data, append=True)


if __name__ == '__main__':
    from random import randint, uniform
    from sem7_package.tools import writer

    gen(count=51)
