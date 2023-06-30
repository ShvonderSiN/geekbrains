# Задание №4
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.


gen = (num for num in range(101) if sum(int(digit) for digit in str(num)) != 8)

# print(*gen)

for _ in gen:
    print(next(gen))
