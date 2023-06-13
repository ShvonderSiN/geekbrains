import csv


def read_scv(csv_file) -> list:
    """
    Печатает содержимое CVS файла в консоль
    """
    try:
        with open(csv_file, encoding='utf-8') as file:
            reader = csv.DictReader(f=file, delimiter=';')
            return [row for row in reader]
    except FileNotFoundError:
        print('Файл не найден')


def write_csv(csv_file, text, fields) -> None:
    """
    Записывает в CSV файл данные
    """
    with open(csv_file, 'w+', encoding='utf-8', newline='\n') as file:
        writer = csv.DictWriter(f=file, fieldnames=fields, delimiter=';')
        writer.writeheader()
        writer.writerows(text)
