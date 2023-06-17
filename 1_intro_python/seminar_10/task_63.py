"""
Задача №63. Решение в группах
1. Изобразите отношение households к population с
помощью точечного графика
2. Визуализировать longitude по отношения к
median_house_value, используя линейный график
3. Представить гистограмму по housing_median_age
4. Изобразить гистограмму по median_house_value с
оттенком housing_median_age
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('california_housing_test.csv')


def task_1(array) -> None:
    """
    Изобразите отношение households к population
    """
    households = array.households
    population = array.population
    plt.scatter(x=households, y=population)
    plt.xlabel('Владельцы')
    plt.ylabel('Популяция')
    plt.title('Отношение households к population')
    plt.show()


def task_2(array) -> None:
    """
    Визуализирует longitude по отношения к median_house_value
    """
    plt.plot(array.longitude, array.median_house_value)
    plt.title('Отношение longitude к median_house_value')
    plt.show()


def task_3(array, bin_num=5, color='blue') -> None:
    """
    Представляет гистограмму по housing_median_age
    """
    plt.hist(array.housing_median_age, bins=bin_num, color=color)
    plt.title('Гистограмма по housing_median_age')
    plt.show()


def task_4(array) -> None:
    """
    Изображает гистограмму по median_house_value с оттенком housing_median_age
    """
    sb.histplot(data=array, x='median_house_value', hue='housing_median_age')
    plt.title('Гистограмма по median_house_value с оттенком housing_median_age')
    plt.show()


if __name__ == '__main__':
    task_1(data)
    task_2(data)
    task_3(data, bin_num=10, color='green')
    task_4(data)
