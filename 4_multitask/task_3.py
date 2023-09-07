# Задание №3
# � Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
# адреса.
# � После загрузки данных нужно записать их в отдельные
# файлы.
# � Используйте асинхронный подход.
import aiofiles
import aiohttp
import asyncio

from task_1 import urls, time_decorator


@time_decorator
async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'task_3_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            async with aiofiles.open('task_3/' + filename, 'w', encoding='utf-8') as f:
                await f.write(text)


async def main():
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download(url))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
