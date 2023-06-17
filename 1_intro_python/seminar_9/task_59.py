"""
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и
median_house_value > 70000
"""
import pandas as pd

data = pd.read_csv('sample_data/california_housing_test.csv')
#  1
print('1 ' + '#' * 50)
print(data.isna().sum())
#  не понял в чем тут разница, наверное если читать из бд, то разница будет...
#  в csv ведь нет нулл значения
print(data.isnull().sum())
#  2
print('2 ' + '#' * 50)
print(data['median_house_value'][data['median_income'] < 2])
print(data.loc[data['median_income'] < 2, 'median_house_value'])
#  3
print('3 ' + '#' * 50)
print(data.iloc[:, :2])
print(data.loc[:, 'longitude': 'latitude'])
print(data[['longitude', 'latitude']])
#  4
print('4 ' + '#' * 50)
print(data[(data['housing_median_age'] < 20) & (data['median_house_value'] > 70000)])
