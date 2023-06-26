"""Напишите функцию, которая принимает строку текста.
✔ Сформируйте список с уникальными кодами Unicode каждого
символа введённой строки отсортированный по убыванию.
"""


def unicode_string(s: str) -> list:
    return sorted(set(ord(char) for char in s), reverse=True)


print(unicode_string('Hello World Fellas'))
