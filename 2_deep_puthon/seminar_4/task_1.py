""" Напишите функцию, которая принимает строку текста.
Вывести функцией каждое слово с новой строки.
✔ Строки нумеруются начиная с единицы.
✔ Слова выводятся отсортированными согласно кодировки Unicode.
✔ Текст выравнивается по правому краю так, чтобы у самого
длинного слова был один пробел между ним и номером строки."""


def string_splitter(s: str = '') -> list:
    if s:
        s = s.split()
        s.sort()
        return s
    raise ValueError('No string provided')


string = 'Hello World Guys Parabellum'
# max_len = max(len(word) for word in string_splitter(string))
#  удалось посмотреть часть лекции, решил дописать как можно max использовать еще
max_len = len(max(string_splitter(string), key=lambda x: len(x)))

for num, w in enumerate(string_splitter(string), 1):
    print(f'{num}, {w.rjust(max_len)}')
