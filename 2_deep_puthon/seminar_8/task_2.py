# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
from json import JSONDecodeError


def access_log() -> None:
    try:
        with open('task_2_access_log.json', 'r') as file:
            dict_ = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        dict_ = {}
    while True:
        name = input('Введите имя: ')
        level = input('Введите уровень доступа (от 1 до 7): ')
        if level and level.isdigit():
            level = int(level)
        else:
            print('Уровень доступа должен быть целым числом.')
            continue
        if level < 1 or level > 7:
            print('Уровень доступа должен быть в диапазоне от 1 до 7.')
            continue
        id_ = input('Введите личный идентификатор: ')

        if dict_.get(id_, {}):
            print('Идентификатор уже существует. Повторите ввод.')
            continue

        dict_[id_] = {}
        dict_[id_]['level'] = level
        dict_[id_]['name'] = name
        # Сохранение данных в файл
        dict_ = dict(sorted(dict_.items(), key=lambda x: int(x[1]['level'])))
        print(dict_.items())
        with open('task_2_access_log.json', 'w') as file:
            json.dump(dict_, file, ensure_ascii=False, indent=4)
        choice = input('Хотите продолжить ввод данных? (y/n): ')
        if choice.lower() == 'n':
            break


if __name__ == '__main__':
    access_log()
