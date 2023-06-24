"""
Задание 1
Вручную создайте список с целыми числами, которые повторяются.
Получите новый список, который содержит уникальные
(без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное,
которое не использует другие коллекции помимо списков."""

lst = [1, 3, 6, 3, 8, 23, 3, 8, 55]


def unique(x: list) -> list:
    """Короткое решение"""
    x = list(set(x))
    x.sort()
    return x


def long_unique(x: list) -> list:
    """Длинное решение"""
    # так же можно решить с помощью метода pop()
    new_lst = []
    for i in x:
        if i not in new_lst:
            new_lst.append(i)
        continue
    new_lst.sort()
    return new_lst


if '__main__' == __name__:
    unique_lst = unique(lst)
    print(lst, unique_lst, sep='\n')

    unique_lst2 = long_unique(lst)
    print(lst, unique_lst2, sep='\n')
