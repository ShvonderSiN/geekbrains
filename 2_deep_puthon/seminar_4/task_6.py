"""✔ Функция получает на вход список чисел и два индекса.
✔ Вернуть сумму чисел между между переданными индексами.
✔ Если индекс выходит за пределы списка, сумма считается
до конца и/или начала списка."""

nums = [1, 3, 67, 72, 8, 3, 3.4]


def sum_numbers(numbers: list, index1: int, index2: int) -> float | int:
    if not all(isinstance(num, (int, float)) for num in numbers):
        return 'В коллекции должны быть только цифры'
    try:
        num1 = numbers[index1]
    except IndexError:
        num1 = None
    try:
        num2 = numbers[index2]
    except IndexError:
        num2 = None
    if num1 and num2:
        return num1 + num2
    elif not num1:
        new = numbers[:index2]
        return sum(new)
    elif not num2:
        new = numbers[index1:]
        return sum(new)
    else:
        return sum(numbers)


print(sum_numbers(nums, 1, 3))
print(sum_numbers(nums, 3, 12))
print(sum_numbers(nums, -1, 2))

nums += ['1']  # Добавил строку в список
print(sum_numbers(nums, 1, 4))
