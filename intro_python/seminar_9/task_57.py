"""
Прочесть с помощью pandas файл
california_housing_test.csv, который находится в папке
sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""
import pandas as pd

data = pd.read_csv('sample_data/california_housing_test.csv')
#  кол-во строк
print(len(data.index), '\n' + 'or')
print(len(data), '\n' + '#' * 30)
#  кол-во колонок
print(len(data.columns), '\n' + '#' * 30)
#  Можно вывести строки и колонки кортежем
print(data.shape)
#  тип данных столбцов
print(data.dtypes)
