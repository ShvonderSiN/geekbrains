# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """Класс Архив"""
    lst = []

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string
        Archive.lst.append((self.number, self.string))

    def __repr__(self):
        return f'{Archive.__name__}: ({self.number}, {self.string})'

    def __str__(self):
        return f'{self.number}, {self.string}'


if __name__ == '__main__':
    a = Archive(5, 'Sergei')
    b = Archive(6, 'Vasya')

    print(repr(a))
    print(b)
