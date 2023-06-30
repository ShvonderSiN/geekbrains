# Задание №6
# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.


# Сначала вспомнил как это делается
# for i in range(2, 11):
#   for j in range(2, 11):
#     print(f'{i} x {j} = {i * j}')
#   print()

table_gen = (f'{i} x {j} = {i * j}' for j in range(2, 11) for i in range(2, 11))

# for i in list(table_gen):
#     print(i, end=' ###')

print(next(table_gen))
print(next(table_gen))
print(next(table_gen))
print(next(table_gen))
