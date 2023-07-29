# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.
import sys

import numpy


class Matrix:
    """
    Матрица. Класс для создания матриц, а так же:
        ○ вывода на печать,
        ○ сравнения,
        ○ сложения,
        ○ умножения матриц
    """

    def __init__(self, *args):
        try:
            self.matrix = numpy.array(args)
        except ValueError as er:
            print(f'{er}\nПроверьте переданные аргументы матрицы, ее геометрия не правильная')
            sys.exit(0)

    def show_matrix(self) -> str:
        """
        СТроит матрицу и показывает
        Returns: str
        """
        s = """"""
        for row in self.matrix:
            row_str = " ".join(f'{str(elem):3s}' for elem in row)
            s += row_str + "\n"
        return s

    def __str__(self):
        return numpy.array_str(self.matrix)

    def __add__(self, other):
        try:
            matrix = Matrix(*numpy.add(self.matrix, other.matrix))
        except ValueError as er:
            print(f'{er}\nДве матрицы можно сложить, если их размеры совпадают.')
        else:
            return matrix

    def __mul__(self, other):
        try:
            matrix = Matrix(*numpy.multiply(self.matrix, other.matrix))
        except ValueError as er:
            print(f'{er}\nМатрицы можно перемножить, если число столбцов первой \
                    матрицы равно числу строк второй матрицы.')
        else:
            return matrix

    def __eq__(self, other):
        return numpy.array_equal(self.matrix, other.matrix)


if __name__ == '__main__':
    m1 = Matrix([1, 2, 3],
                [4, 5, 6],
                [7, 8, 9])
    m2 = Matrix([1, 2, 3],
                [4, 5, 6],
                [7, 8, 9])
    print(m1.show_matrix())

    m3 = m1 + m2
    print(m3.show_matrix())

    m4 = m1 * m2
    print(m4.show_matrix())

    # сравнение матриц
    print(f'{m1 == m2 = }')
    print(f'{m1 != m2 = }')
