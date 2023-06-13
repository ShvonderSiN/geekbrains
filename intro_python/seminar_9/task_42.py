"""
Задача 42: Узнать какая максимальная households в зоне минимального значения population.
"""
import pandas as pd

data = pd.read_csv('sample_data/california_housing_test.csv')
min_population = data['population'].min()
print('Maximum households is:', data[data['population'] == min_population]['households'].max())
