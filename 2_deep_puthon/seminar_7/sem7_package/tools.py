import os

from random import randint, choice

__all__ = ['writer', 'names_generator', 'file_renamer']


def writer(path: str, data: str, append: bool = False) -> None:
    """Записывает в файл
    path = Путь до файла str
    data = Данные, которые пишем str
    append = Режим До записи или перезаписи bool, default w+
    """
    mode = 'a+' if append else 'w+'
    with open(path, mode=mode, encoding='utf-8') as f:
        f.write(data)


_glas_letters = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')
_alphabet = (
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М',
    'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ',
    'Ы', 'Ь', 'Э', 'Ю', 'Я'
)


def names_generator() -> str:
    list_of_letters = []
    count = length = randint(4, 7)
    while count > 0:
        letter = choice(_alphabet).upper()
        count -= 1
        list_of_letters.append(letter)
        if not count and not any(glass.upper() in list_of_letters for glass in _glas_letters):
            count = length
            list_of_letters.clear()
    return ''.join(list_of_letters).title() + '\n'


def file_renamer(dir_: str = '.', new_file_name: str = '', new_ext: str = '',
                 prefix_num: int = None, old_ext: str = None, range_: tuple = None) -> None:
    """Переименовывает файлы в выбранной директории и ее поддиректориях"""
    file_list_for_rename = []  # Формирую список файлов для переименования
    exclude_dirs = ('venv',)  # Исключаю не нужные директории
    #  Иду по директориям, собираю файлы
    for root, dirs, files in os.walk(dir_):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]  # Исключаю из поиска ненужные директории
        for file in files:
            if file.endswith(old_ext):
                file_list_for_rename.append(os.path.join(root, file))

    # формирую новое имя
    prefix_counter = 0
    for file in file_list_for_rename:
        prefix_counter += 1
        if range_ and new_file_name:
            new_name = new_file_name + os.path.splitext(os.path.basename(file))[0][range_[0]:range_[1] + 1]
        elif new_file_name:
            new_name = new_file_name
        elif range_:
            new_name = os.path.splitext(os.path.basename(file))[0][range_[0]:range_[1] + 1]
        else:
            new_name = os.path.splitext(os.path.basename(file))[0]
        if prefix_num:
            # вот тут я сначала застрял, пришлось искать как сделать форматирование
            new_name += '_{:0{}d}'.format(prefix_counter, prefix_num)

        new_ext = new_ext if new_ext else os.path.splitext(os.path.basename(file))[1]
        result = os.path.normpath(os.path.join(os.path.dirname(file), new_name + new_ext))
        print(result)
        #  чтобы не ломать файлы я не стал реализовывать реальное переименование
