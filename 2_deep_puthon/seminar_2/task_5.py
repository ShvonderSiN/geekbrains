"""
№5
Задачи для сессионных залов:
Напишите программу, которая решает квадратные уравнения даже если
дискриминант отрицательный.
Используйте комплексные числа
для извлечения квадратного корня.
"""
import cmath, math

a = float(input('Число A: '))
b = float(input('Число B: '))
c = float(input('Число C: '))

D = (b ** 2) - (4 * a * c)

root_1 = (-b + cmath.sqrt(D)) / (2 * a)
root_2 = (-b - cmath.sqrt(D)) / (2 * a)
# root_1_math = (-b + math.sqrt(D)) / (2 * a)
# root_2_math = (-b - math.sqrt(D)) / (2 * a)


print("Корень 1:", root_1.real, "Корень 2:", root_2.real)
# print("Корень  math:", root_1_math, "Корень 2 math:", root_2_math)
