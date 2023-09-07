# Задание №8
# � Напишите программу, которая будет скачивать страницы из
# списка URL-адресов и сохранять их в отдельные файлы на
# диске.
# � В списке может быть несколько сотен URL-адресов.
# � При решении задачи нужно использовать многопоточность
import threading
import time

import requests
import os

from task_1 import time_decorator

urls = ['https://megaseller.shop/', 'https://render.com/', 'https://snyk.io/']


@time_decorator
def website(url: str, save_dir: str) -> None:
    try:
        response = requests.get(url)
        filename = os.path.join(save_dir,
                                url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html")
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"Успешно скачано: {url}")
    except Exception as e:
        print(f"Не удалось скачать {url}. Ошибка: {e}")


if __name__ == '__main__':
    path = os.path.join('.', 'task_8_1')
    threads = []
    for url in urls:
        thread = threading.Thread(target=website, args=[url, path], daemon=True)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Успешно скачано: https://megaseller.shop/
# Время выполнения функции 'website': 0.9263 секунд
# Успешно скачано: https://snyk.io/
# Время выполнения функции 'website': 1.1463 секунд
# Успешно скачано: https://render.com/
# Время выполнения функции 'website': 1.2401 секунд
