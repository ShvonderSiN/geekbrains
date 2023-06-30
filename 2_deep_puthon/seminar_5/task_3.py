# Задание №3
# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

COUNT = 5

d = {
    'С': 1057, 'а': 1072, 'м': 1084, 'о': 1086,
    'с': 1089, 'т': 1090, 'я': 1103, 'е': 1077,
    'л': 1083, 'ь': 1100, 'н': 1085, ' ': 32,
    'х': 1093, 'р': 1088, 'и': 1080, 'в': 1074,
    'п': 1087, 'й': 1081, 'к': 1082, 'у': 1091,
    '.': 46
}

d = iter(d.items())

for _ in range(COUNT):
    k, v = next(d)
    print(f'{k = }, {v = }')
