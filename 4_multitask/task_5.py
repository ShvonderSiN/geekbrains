# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.
import multiprocessing
import os

from task_4 import count_words_in_files

if __name__ == '__main__':
    processes = []
    files = os.listdir('.')

    for file in files:
        full_path = os.path.join('.', file)
        if os.path.isfile(full_path):
            proc = multiprocessing.Process(target=count_words_in_files, args=(full_path,), daemon=True)
            processes.append(proc)
            proc.start()

    for proc in processes:
        proc.join()
# .\task_1.py 166
# .\task_2.py 91
# .\task_3.py 113
# .\task_4.py 131
# .\task_5.py 72
# .\task_6.py 143
# .\task_7_1.py 188
# .\task_7_2.py 179
# .\task_7_3.py 230
# .\task_8_1.py 73
# .\task_8_2.py 76
# .\task_8_3.py 80
