# Задание №1
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте потоки.
import threading
import time
import requests
from functools import wraps

urls = [
    'https://www.google.ru/',
    'https://gb.ru/',
    'https://ya.ru/',
    'https://www.python.org/',
    'https://habr.com/ru/all/',
    'https://yandex.ru/',
    'https://mail.ru/',
    'https://brainycp.com',
    'https://render.com/',
    'https://snyk.io/'
]


def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции '{func.__name__}': {end_time - start_time:.8f} секунд")
        return result

    return wrapper


@time_decorator
def download(url):
    response = requests.get(url)
    filename = 'task_1_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open('task_1/' + filename, 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__ == '__main__':
    threads = []

    for url in urls:
        thread = threading.Thread(target=download, args=(url,), daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
