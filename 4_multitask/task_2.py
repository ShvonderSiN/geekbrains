# Задание №2
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте процессы.
# Задание №1
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.
import multiprocessing
from task_1 import urls, download

if __name__ == '__main__':
    processes = []

    for url in urls:
        proc = multiprocessing.Process(target=download, args=(url,), daemon=True)
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()
