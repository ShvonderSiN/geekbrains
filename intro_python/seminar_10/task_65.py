"""
Задача №65. Решение в группах
Написать EDA для датасета про пингвинов
Необходимо:
● Использовать 2-3 точечных графика
● Применить доп измерение в точечных графиках, используя
аргументы hue, size, stile
● Использовать PairGrid с типом графика на ваш выбор
● Изобразить Heatmap
● Использовать 2-3 гистограммы
Чтобы подключить датасет с
пингвинами, воспользуйтесь данным
скриптом:
penguins = sns.load_dataset("penguins")
penguins.head()
"""

import matplotlib.pyplot as plt
import seaborn as sb

data = sb.load_dataset('penguins')

print(data.head())


def task_1(array) -> None:
    """
    Использовать 2-3 точечных графика
    """
    plt.scatter(array['bill_length_mm'], array['body_mass_g'])
    plt.show()

    plt.scatter(array['bill_depth_mm'], array['flipper_length_mm'])
    plt.show()

    plt.scatter(array['body_mass_g'], array['bill_depth_mm'])
    plt.show()


def task_2(array) -> None:
    """
    Применяю доп измерение в точечных графиках, используя
    аргументы hue, size, stile
    """
    sb.catplot(x='body_mass_g', y='bill_length_mm', data=array, hue='species')
    plt.show()
    sb.pointplot(x='body_mass_g', y='bill_length_mm', data=array, hue='island')
    plt.show()


def task_3(array) -> None:
    """
    Использовать PairGrid с типом графика на ваш выбор
    """
    sb.pairplot(array, hue='species')
    plt.show()
    sb.pairplot(array, height=10)
    plt.show()


def task_4(array) -> None:
    """
    Изображаю Heatmap
    """
    new_array = array[['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']]
    sb.heatmap(new_array.corr(), annot=True, cmap="coolwarm")
    plt.show()


def task_5(array) -> None:
    """
    Использовать 2-3 гистограммы
    """
    sb.histplot(array['bill_length_mm'], bins=10)
    plt.show()

    sb.histplot(array['bill_depth_mm'], bins=10, cbar=True)
    plt.show()

    sb.histplot(array['sex'], bins=10, kde=True)
    plt.show()


if __name__ == '__main__':
    task_1(data)
    task_2(data)
    task_3(data)
    task_4(data)
    task_5(data)
