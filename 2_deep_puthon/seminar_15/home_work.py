# Напишите код, который запускается из командной строки
# и получает на вход путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple. Каждый объект хранит:
# имя файла без расширения или название каталога,
# расширение, если это файл,
# флаг каталога,
# название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import logging
import os
from collections import namedtuple

logging.basicConfig(filename='home_work.log', level=logging.INFO, style='{',
                    format='{levelname} - {asctime} - {name} - {msg}', encoding='utf-8', filemode='a', )
logger = logging.getLogger(f'{__name__} ({os.path.basename(__file__)})')


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    return parser.parse_args()


path = os.path.normpath(get_args().path)

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

for root, dirs, files in os.walk(path):
    for file_name in files:
        name, extension = os.path.splitext(file_name)
        info = FileInfo(name=name, extension=extension if extension else None, is_directory=False,
                        parent_directory=root)
        logger.info(info)

    for directory in dirs:
        info = FileInfo(name=directory, extension=None, is_directory=True, parent_directory=root)
        logger.info(info)

# INFO - 2023-08-10 23:29:17,903 - __main__ (home_work.py) - FileInfo(name='home_work', extension='.log', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,903 - __main__ (home_work.py) - FileInfo(name='home_work', extension='.py', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,903 - __main__ (home_work.py) - FileInfo(name='task_1', extension='.py', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,903 - __main__ (home_work.py) - FileInfo(name='task_2', extension='.py', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,957 - __main__ (home_work.py) - FileInfo(name='task_3', extension='.py', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,957 - __main__ (home_work.py) - FileInfo(name='test_folder', extension=None, is_directory=True, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15')
# INFO - 2023-08-10 23:29:17,958 - __main__ (home_work.py) - FileInfo(name='test_file', extension='.png', is_directory=False, parent_directory='C:\\Projects\\geekbrains\\2_deep_puthon\\seminar_15\\test_folder')
