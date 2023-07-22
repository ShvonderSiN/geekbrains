# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц

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
        self.matrix = numpy.array(args)

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
        return Matrix(*numpy.add(self.matrix, other.matrix))

    def __mul__(self, other):
        return Matrix(*numpy.multiply(self.matrix, other.matrix))

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

    try:
        m3 = m1 + m2
    except ValueError:
        print('Две матрицы можно сложить, если их размеры совпадают.')
    else:
        print(m3.show_matrix())

    try:
        m4 = m1 * m2
    except ValueError:
        print('Матрицы можно перемножить, если число столбцов первой матрицы равно числу строк второй матрицы.')
    else:
        print(m4.show_matrix())

    # сравнение матриц
    print(f'{m1 == m2 = }')
    print(f'{m1 != m2 = }')
