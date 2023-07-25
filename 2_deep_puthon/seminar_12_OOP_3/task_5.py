# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__

class Rectangle:
    """
    Class Rectangle
    """
    __slots__ = '__width', '__length'

    def __init__(self, width: int | float, length: int | float = 0):
        self.width = width
        self.length = length

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validator(value)
        self.__width = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__validator(value)
        self.__length = value

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

    @classmethod
    def __validator(cls, value):
        if value <= 0:
            raise ValueError('Значение должно быть положительным')

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
