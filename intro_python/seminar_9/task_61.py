"""
1. Определить какое максимальное и минимальное
значение median_house_value
2. Показать максимальное median_house_value, где
median_income = 3.1250
3. Узнать какая максимальная population в зоне
минимального значения median_house_value
"""

import pandas as pd

data = pd.read_csv('sample_data/california_housing_test.csv')

#  1
print('1 ' + '#' * 50)
maximum = data['median_house_value'].max()
minimum = data['median_house_value'].min()
print('Maximum is:', maximum)
print('Minimum is:', minimum)

#  2
print('2 ' + '#' * 50)
maximum_median_house_value = data[data['median_income'] == 3.1250]['median_house_value'].max()
print('Maximum median_house_value is:', maximum_median_house_value)
#  3
print('3 ' + '#' * 50)
minimum_zone = data['median_house_value'].min()
max_population = data[data['median_house_value'] == minimum_zone]['population'].max()
print('max_population is:', max_population)
