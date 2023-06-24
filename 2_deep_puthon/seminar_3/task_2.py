"""
Задание 2
Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:

целое положительное число
вещественное положительное или отрицательное число
строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
строку в верхнем регистре в остальных случаях"""

data = input('Введите строку: ')

if data.isdigit():
    print(int(data))

elif data.replace('.', '', 1).isdigit() or data.startswith('-'):
    print(float(data))

elif data.isalpha():
    if any(i.isupper() for i in data):
        print(data.lower())
    else:
        print(data.upper())

else:
    print('Спасибо за участие!')
