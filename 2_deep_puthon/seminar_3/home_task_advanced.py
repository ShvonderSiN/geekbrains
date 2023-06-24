"""Дополнительно:
Задача 1:
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
Верните все возможные варианты комплектации рюкзака.
"""

MAX_WEIGHT = 10
things = {
    'Лопата': 1,
    'Фонарь': 0.5,
    'Еда': 2,
    'Палатка': 7,
    'Колонка': 2,
    'Вода': 4
}


def calc_back_pack(stuff: dict, max_weight: (int, float) = 5) -> (int, list):
    """Верните все возможные варианты комплектации рюкзака"""
    keys = list(stuff.keys())
    random.shuffle(keys)

    back_pack = 0
    things = []
    for key in keys:
        if back_pack + stuff[key] <= max_weight and stuff[key] <= max_weight:
            back_pack += stuff[key]
            things.append(key)
        else:
            continue
    return back_pack, things


"""
Задача 2:
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей.
Ответьте на вопросы:
** какие вещи взяли все три друга
** какие вещи уникальны, есть только у одного друга
** какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами.
Код должен расширяться на любое большее количество друзей. 
(часть уже сделана на семинаре и лежит на гите"""

friends = {
    'Сергей': ('fishing rod', 'lighter', 'tent'),
    'Алексей': ('tent', 'brazier', 'gun'),
    'Володя': ('tent', 'gun', 'sun cream')
}


def friends_calc(friends: dict) -> None:
    all_items = set(item for items in friends.values() for item in items)
    print(f'Друзья вместе взяли эти вещи: {all_items}')

    missing_items = {f: all_items - set(friends[f]) for f in friends}
    for friend, items in missing_items.items():
        if items:
            print(f"{friend} не взял: {items}")
        else:
            print(f"{friend} взял все вещи")

    for name1 in friends:
        unique_items = set(friends[name1])
        for name2 in friends:
            if name1 != name2:
                unique_items -= set(friends[name2])
        print(f'{name1} имеет при себе следующие уникальные вещи: {unique_items}')


if __name__ == '__main__':
    import random
    stuff = calc_back_pack(things, MAX_WEIGHT)
    print(stuff[0], *stuff[1])

    friends_calc(friends)
