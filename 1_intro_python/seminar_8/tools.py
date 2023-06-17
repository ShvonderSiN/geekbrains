from utils import write_csv, read_scv


def find_info(file, search) -> list:
    found = []
    row_number = -1
    for row in file:
        row = f"{row['surname']} {row['name']} {row['patronymic']} {row['phone']}".lower()
        row_number += 1
        if search.lower() in row:
            found.append((row_number, row))
    print(f'Найдено {len(found)} человек:')
    for men in found:
        print(men[1].title())
    return found


def edit_info(founded):
    reader = read_scv('test.csv')
    for row in founded:
        name = input('Введите новое имя или оставьте без изменений: ')
        if name:
            reader[row[0]]['name'] = name
        surname = input('Введите новую фамилию или оставьте без изменений: ')
        if surname:
            reader[row[0]]['surname'] = surname
        patronymic = input('Введите новое отчество или оставьте без изменений: ')
        if patronymic:
            reader[row[0]]['patronymic'] = patronymic
        phone = input('Введите новый телефон или оставьте без изменений: ')
        if phone:
            reader[row[0]]['phone'] = phone
    write_csv('test.csv', reader, field_names)
    print("База успешно обновлена")
