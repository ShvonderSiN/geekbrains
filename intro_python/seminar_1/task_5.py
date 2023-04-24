'''

Задача 6: Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, 
где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

Пример:

385916 -> yes
123456 -> no
'''


def sum_digits(number) -> int:
    '''Возвращает сумму цифр трехзначного числа'''
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


def check_number_length(number) -> bool:
    '''Проверяет длину числа на четность'''
    if len(str(number)) // 2 == 0:
        return True
    return False


ticket_number = input('Введите номер билета: ').strip()
first_three = sum_digits(int(ticket_number[:3]))
last_three = sum_digits(int(ticket_number[3:6]))

if check_number_length(ticket_number):
    print('Введите четное количество номера билета')
elif first_three == last_three:
    print(f'{ticket_number} -> yes')
else:
    print(f'{ticket_number} -> no')
