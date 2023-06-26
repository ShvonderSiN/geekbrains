"""Функция принимает на вход три списка одинаковой длины:
✔ имена str,
✔ ставка int,
✔ премия str с указанием процентов вида «10.25%».
✔ Вернуть словарь с именем в качестве ключа и суммой
премии в качестве значения.
✔ Сумма рассчитывается как ставка умноженная на процент премии."""

names = ['Valera', 'Sergei', 'Igor']
day_rate = [1050, 2030, 3010]
extra = ["10.25%", "5%", "12%"]


def premium(names: list, day_rate: list, extra: list) -> dict:
    dict_premium = {}
    for i in range(len(names)):
        dict_premium[names[i]] = (float(extra[i].replace('%', '')) * day_rate[i]) / 100
    return dict_premium


for name, prem in premium(names, day_rate, extra).items():
    print(name, prem)
