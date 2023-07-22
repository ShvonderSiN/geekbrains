# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
from time import time


class MyString(str):
    """Класс Моя Строка, расширяет встроенный класс str"""

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.time = time()
        return instance

    def __repr__(self):
        return f'MyString({self}, {self.author}, {self.time})'


if __name__ == '__main__':
    st_1 = MyString(value='String', author='Vasya')
    print(st_1.author.upper(), st_1.time)
    print(repr(st_1))
