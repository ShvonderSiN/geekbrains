# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


names = ['Sergei', 'Vlad', 'Boris', 'Ivan']
rates = [1000, 3000, 5000, 1500]
p = ['10.25%', '10.15%', '10.35%', '10.05%']


def extra_dict(names: list[str] = None,
               rates: list[int] = None,
               p: list[str] = None) -> dict[str, float]:
    p = (float(i[:-1]) / 100 for i in p)

    return {name: rate * perc for name, rate, perc in zip(names, rates, p)}


# print(extra_dict(names, rates, p))
for k, v in extra_dict(names, rates, p).items():
    print(k, v)
