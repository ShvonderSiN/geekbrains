#  Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.


path = r'/home/runner/GeekBrains/task_1.py'


def path_splitter(path: str) -> tuple:
    """решение"""
    *path, file = path.split('/')
    file_name, ext = file.split('.')

    return '/'.join(path), file_name, ext


def path_splitter_2(path: str) -> tuple:
    """Рекомендуют с путями работать спец средствами
    так, как пути могут отличаться в разных системах"""
    catalog, file = os.path.dirname(path), os.path.basename(path)

    return catalog, *os.path.splitext(file)  # здесь оставляет точку, ее можно убрать replace('.', '')


if __name__ == '__main__':
    print(path_splitter(path))
    import os

    print(path_splitter_2(path))
