# Задание
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать мультипроцессорный подход.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.

import requests
import multiprocessing

from _pytest import pathlib
from bs4 import BeautifulSoup
from task_3 import time_decorator


def get_image_urls(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    figures = soup.find_all('figure')
    links = [figure.find('img').get('data-lazy-src') for figure in figures]
    return links


def img_downloader(url):
    response = requests.get(url)
    filename = pathlib.Path(url).name
    if not pathlib.Path.exists(pathlib.Path('home_2')):
        pathlib.Path('home_2').mkdir()
    with open('home_2/' + filename, 'wb') as f:
        f.write(response.content)


@time_decorator
def main():
    urls = get_image_urls('https://bigpicture.ru/100-luchshix-fotografij-koshek-vsex-vremen-i-narodov/')
    processes = []
    for url in urls:
        proc = multiprocessing.Process(target=img_downloader, args=(url,), daemon=True)
        proc.start()
    for proc in processes:
        proc.join()


if __name__ == '__main__':
    main()

    # Время выполнения функции 'main': 15.7489 секунд
