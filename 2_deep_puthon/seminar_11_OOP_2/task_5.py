# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """
    Class Rectangle
    """

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


if __name__ == '__main__':
    r, s = Rectangle(1, 2), Rectangle(3, 4)

    square, perimeter = r.square(), r.perimeter()
    print(f"{square = }, {perimeter = }")

    square, perimeter = s.square(), s.perimeter()
    print(f"{square = }, {perimeter = }")

    n = r + s
    print(f'{r + s = }')
    square, perimeter = n.square(), n.perimeter()
    print(f"{square = }, {perimeter = }")

    n = r - s
    print(f'{r - s = }')
    square, perimeter = n.square(), n.perimeter()
    print(f"{square = }, {perimeter = }")
