# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

# я не понял что от меня хотят, у меня нет таких декораторов...
# проверка в методе валидаторе организована

class RectangleChecker:
    """Дескриптор, проверяет длину и ширину прямоугольника"""

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__validate(value)
        return setattr(instance, self.name, value)

    def __validate(self, value):
        if value <= 0:
            raise ValueError('Длина и ширина должны быть положительным числом')


class Rectangle:
    """
    Class Rectangle
    """
    # __slots__ = 'width', 'length'   как я понял, слоты тут не работают так как привязан дескриптор
    width = RectangleChecker()
    length = RectangleChecker()

    def __init__(self, width: int | float, length: int | float = 0):
        self.width = width
        self.length = length

    def __add__(self, other):
        p = self.perimeter() + other.perimeter()
        a = (p // 2) - self.width
        b = (p // 2) - a
        return Rectangle(a, b)

    def __sub__(self, other):
        p = abs(self.perimeter() - other.perimeter())
        side = abs(self.width - other.width)
        a = (p / 2) - side
        b = (p / 2) - a
        return Rectangle(a, b)

    def square(self) -> int | float:
        """Returns: square, (int, float)"""
        if not self.length:
            return self.width ** 2
        return self.width * self.length

    def perimeter(self) -> int | float:
        """Returns: Perimeter of rectangle, (int, float)"""
        if not self.length:
            return 4 * self.width
        return 2 * (self.width + self.length)

    def __repr__(self):
        return f'{Rectangle.__name__}({self.width}, {self.length})'

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()


if __name__ == '__main__':
    r = Rectangle(3, 1)
    print(r.width)
    r.length = -1
    print(r.length)
