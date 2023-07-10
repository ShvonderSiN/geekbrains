# Задание №4
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json


def reader_csv(file_name: str) -> tuple:
    """
    Читает csv файл, отдает tuple"""
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = tuple(csv.reader(f))
        return reader


def processor_csv(reader) -> list[dict]:
    """
    Обрабатывает полученные данные из файла в список словарей"""
    new = []
    for row in reader[1:]:
        new_name = row[1].title()
        new_id = row[0].zfill(10)
        hash_ = hash(new_id)
        new.append({'ID': new_id, 'NAME': new_name, 'LEVEL': row[2], 'HASH_ID': hash_})
    return new


def record_to_json(old_file: str, new_file: str) -> None:
    """
    Конвертирование из CSV в JSON
    old_file: имя исходного файла
    new_file: имя конечного файла"""
    old = reader_csv(old_file)
    proc = processor_csv(old)
    with open(new_file, 'w+', encoding='utf-8') as f:
        json.dump(proc, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    record_to_json('task_3_access_log.csv', 'task_4_access_log.json')
