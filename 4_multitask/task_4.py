# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.

import os
import re
import threading


def count_words_in_files(file):
    with open(file, encoding='utf-8') as f:
        text = f.read()
        words = re.findall(r'\b\w+\b', text)
        print(file, len(words))


if __name__ == '__main__':
    threads = []
    files = os.listdir('.')
    for file in files:
        full_path = os.path.join('.', file)
        if os.path.isfile(full_path):
            thread = threading.Thread(target=count_words_in_files, args=(full_path,), daemon=True)
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
# .\task_1.py 166
# .\task_2.py 91
# .\task_3.py 113
# .\task_4.py 96
# .\task_5.py 72
# .\task_6.py .\task_7_1.py 188143
#
# .\task_7_2.py 179
# .\task_7_3.py 230
# .\task_8_1.py 73
# .\task_8_2.py 76
# .\task_8_3.py 80
