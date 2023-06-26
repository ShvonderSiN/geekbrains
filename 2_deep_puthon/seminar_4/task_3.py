"""
Функция получает на вход строку из двух чисел через пробел.
✔ Сформируйте словарь, где ключом будет
символ из Unicode, а значением — целое число.
✔ Диапазон пар ключ-значение от наименьшего из введённых
пользователем чисел до наибольшего включительно.
"""


def coder_string(s: str) -> dict | str:
    try:
        l = list(map(int, s.split()))
        l.sort()
        if 2 < len(l) > 2:
            raise IndexError
        start = l[0]
        end = l[1] + 1
    except (ValueError, IndexError) as er:
        return f'{er} ->>>> Введите корректную строку, пример: "25 5"'
    unicode_dict = {}
    for num in range(start, end):
        unicode_dict[chr(num)] = num

    return unicode_dict


print(coder_string('10 7'))
print(coder_string('10 7B'))
print(coder_string('10'))
