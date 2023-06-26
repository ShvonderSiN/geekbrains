"""Задание №7
✔ Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
"""

companies = {
    'Газпром': [1000, -2500, -800, 3500],
    'Роснефть': [-500, 750, 1500],
    'Лукойл': [400, 300, 2500, -1450, 500, -3100]
}


def has_negative_integer(arr) -> bool:
    return any(num < 0 for num in arr)


def profit_calc(d: dict = None) -> bool | None:
    if d is None:
        return None

    lst = []
    for company_name, money in d.items():
        profit = sum(money)
        lst.append(profit)
    print(lst)

    return True if not any(num < 0 for num in lst) else False


print(profit_calc(companies))

companies['Лукойл'].append(1000)
print(profit_calc(companies))
