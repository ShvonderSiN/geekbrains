# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

import math


class Circle:
    """
    Class circle
    """

    def __init__(self, radius):
        self.radius = radius

    def length(self) -> float:
        """
        Returns: Length of circle
        """
        return 2 * math.pi * self.radius

    def square(self) -> float:
        """
        Returns: Square of circle
        """
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    c = Circle(5)
    length = c.length()
    square = c.square()
    print(f"Длина окружности: {length}\nПлощадь окружности: {square}")
