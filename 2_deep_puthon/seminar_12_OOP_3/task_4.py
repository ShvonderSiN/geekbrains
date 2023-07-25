# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.
class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self, width: int | float, length: int | float = 0):
        self.width = width
        self.length = length

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self.__validator(value)
        self._width = value

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self.__validator(value)
        self._length = value

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

    def __validator(self, value):
        if value <= 0:
            raise ValueError('Значение не может быть отрицательным')

    def __repr__(self):
        return f'{Rectangle.__name__}({self.width}, {self.length})'

    def __lt__(self, other):
        return self.square() < other.square()

    def __le__(self, other):
        return self.square() <= other.square()

    def __eq__(self, other):
        return self.square() == other.square()


if __name__ == '__main__':
    s = Rectangle(5, 5)
    print(s)
    s.width = 8
    print(s)
    s.width = -1
