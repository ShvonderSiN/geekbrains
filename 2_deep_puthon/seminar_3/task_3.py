"""
Задание 3
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где ключ - тип элемента,
а значение - список элементов данного типа."""

lst = (1, '5', [3, 2], True)

result_dict = {}
for i in lst:
    i_type = type(i)
    if i_type not in result_dict:
        result_dict[i_type] = list()
    result_dict[i_type].append(i)

print(result_dict)
