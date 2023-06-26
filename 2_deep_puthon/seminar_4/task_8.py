"""Задание №8
✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
✔ Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
"""

name = 'sergeis'
company = 'Garlines'
city = 'Murmansks'
letter = 's'


def renamer(s: str) -> str:
    if not (len(s)) == 1 and s.endswith('s') or s.endswith('S'):
        return s[:-1]
    return s


print(renamer(name))
print(renamer(company))
print(renamer(city))
print(renamer(letter))
print(renamer('sS'))
