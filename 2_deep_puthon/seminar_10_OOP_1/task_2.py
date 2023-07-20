# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self, width: int | float, length: int | float = None):
        self.width = width
        self.length = length

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


if __name__ == '__main__':
    r, s = Rectangle(4, 3.3), Rectangle(5.3)

    square, perimeter = r.square(), r.perimeter()
    print(f"{square = }, {perimeter = }")

    square, perimeter = s.square(), s.perimeter()
    print(f"{square = }, {perimeter = }")
