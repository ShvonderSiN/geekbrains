import csv
import json
import pickle

__all__ = ['csv_saver', 'json_saver', 'pickle_saver']


def csv_saver(csv_file_name: str, data: list) -> None:
    """
    Сохраняет в csv файл"""
    with open(csv_file_name, 'w+', encoding='utf-8') as w_file:
        fieldnames = ['Name', 'Type', 'Size', 'Parent Directory']
        writer = csv.DictWriter(w_file, fieldnames=fieldnames, lineterminator='\n')
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def json_saver(json_file_name: str, data: list) -> None:
    """
    Сохраняет в json файл"""
    with open(json_file_name, 'w+', encoding='utf-8') as w_file:
        json.dump(data, w_file, ensure_ascii=False, indent=4)


def pickle_saver(pickle_file_name: str, data: list) -> None:
    """
    Сохраняет в pickle файл"""
    with open(pickle_file_name, 'wb') as w_file:
        pickle.dump(data, w_file, protocol=4)
