# Задание №8
# � Напишите программу, которая будет скачивать страницы из
# списка URL-адресов и сохранять их в отдельные файлы на
# диске.
# � В списке может быть несколько сотен URL-адресов.
# � При решении задачи нужно использовать асинхронность
import multiprocessing
import os
import asyncio, aiohttp, aiofiles

import requests

from task_8_1 import urls
from task_7_3 import time_decorator


@time_decorator
async def website(url: str, save_dir: str) -> None:
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                text = await response.text()
                filename = os.path.join(save_dir,
                                        url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html")
                if not os.path.exists(save_dir):
                    os.makedirs(save_dir)
                async with aiofiles.open(filename, "w", encoding="utf-8") as file:
                    await file.write(text)
                print(f"Успешно скачано: {url}")
    except Exception as e:
        print(f"Не удалось скачать {url}. Ошибка: {e}")


async def main(path):
    tasks = [asyncio.ensure_future(website(url, path)) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    path = os.path.join('.', 'task_8_3')
    asyncio.run(main(path))

# Успешно скачано: https://render.com/
# Время выполнения: 0.15 sec
# Успешно скачано: https://snyk.io/
# Время выполнения: 0.30 sec
# Успешно скачано: https://megaseller.shop/
# Время выполнения: 1.19 sec
