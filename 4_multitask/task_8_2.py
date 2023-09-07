# Задание №8
# � Напишите программу, которая будет скачивать страницы из
# списка URL-адресов и сохранять их в отдельные файлы на
# диске.
# � В списке может быть несколько сотен URL-адресов.
# � При решении задачи нужно использовать многопроцессорность
import multiprocessing
import os
from task_8_1 import urls, website

if __name__ == '__main__':
    path = os.path.join('.', 'task_8_2')
    processes = []
    for url in urls:
        proc = multiprocessing.Process(target=website, args=[url, path], daemon=True)
        processes.append(proc)
        proc.start()

    for proc in processes:
        proc.join()

# Успешно скачано: https://megaseller.shop/
# Время выполнения функции 'website': 0.7971 секунд
# Успешно скачано: https://render.com/
# Время выполнения функции 'website': 0.8792 секунд
# Успешно скачано: https://snyk.io/
# Время выполнения функции 'website': 0.9272 секунд
