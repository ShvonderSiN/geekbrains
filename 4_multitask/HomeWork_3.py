# Задание
# Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск.
# Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
# Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
# — Программа должна использовать асинхронный подход.
# — Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
# — Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.
import sys

import requests
import asyncio
import aiofiles
import aiohttp
import time
import pathlib
from bs4 import BeautifulSoup

args = sys.argv[1:]


def get_image_urls(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    figures = soup.find_all('figure')
    links = [figure.find('img').get('data-lazy-src') for figure in figures]
    return links


async def img_downloader(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            filename = pathlib.Path(url).name
            if not pathlib.Path.exists(pathlib.Path('home_3')):
                pathlib.Path('home_3').mkdir()
            async with aiofiles.open('home_3/' + filename, 'wb') as f:
                await f.write(await response.read())


async def main(url):
    urls = get_image_urls(url)
    tasks = [asyncio.ensure_future(img_downloader(url)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    if args:
        asyncio.run(main(args[0]))
    else:
        asyncio.run(main('https://bigpicture.ru/100-luchshix-fotografij-koshek-vsex-vremen-i-narodov/'))
    end_time = time.time()
    print(f"Время выполнения функции 'main': {end_time - start_time:.4f} секунд")

    # Время выполнения функции 'main': 2.1649 секунд
