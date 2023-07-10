# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json


def reader_json(file: str) -> dict:
    with open(file, 'r', encoding='utf-8') as f:
        file_obj = json.load(f)
        return file_obj


def saver_csv(dict_: dict, file_name: str) -> None:
    """
    dict_: словарь с данными
    file_name: имя файла для сохранения"""
    with open(file_name, 'w+', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['ID', 'NAME', 'LEVEL'], lineterminator='\n')
        writer.writeheader()
        for id_, id_data in dict_.items():
            writer.writerow({'ID': id_, 'NAME': id_data['name'], 'LEVEL': id_data['level']})


if __name__ == '__main__':
    json_dict = reader_json('task_2_access_log.json')
    saver_csv(json_dict, 'task_3_access_log.csv')
