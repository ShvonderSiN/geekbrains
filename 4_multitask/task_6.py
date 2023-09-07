# Задание №6
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте асинхронный подход.
import os
import re
import asyncio
import aiofiles


async def count_words_in_files(file):
    async with aiofiles.open(file, encoding='utf-8') as f:
        text = await f.read()
        words = re.findall(r'\b\w+\b', text)
        print(file, len(words))


async def main(dir_path):
    files = os.listdir(dir_path)
    tasks = []
    for file in files:
        full_path = os.path.join(dir_path, file)
        if os.path.isfile(full_path):
            task = asyncio.ensure_future(count_words_in_files(full_path))
            tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    dir_ = '.'
    asyncio.run(main(dir_path=dir_))
# .\task_1.py 166
# .\task_2.py 91
# .\task_4.py 96
# .\task_6.py 107
# .\task_5.py 72
# .\task_3.py 113
# .\task_7_2.py 179
# .\task_7_3.py 230
# .\task_7_1.py 188
# .\task_8_1.py 73
# .\task_8_3.py 80
# .\task_8_2.py 76
