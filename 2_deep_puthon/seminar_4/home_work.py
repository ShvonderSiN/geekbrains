def make_dict(**kwargs) -> dict | None:
    """
    ✔ Напишите функцию принимающую на вход только ключевые
    параметры и возвращающую словарь, где ключ — значение
    переданного аргумента, а значение — имя аргумента. Если
    ключ не хешируем, используйте его строковое представление.
    """
    if not kwargs:
        return None
    d = {}
    for k, v in kwargs.items():
        try:
            hash(k)
            d[v] = k
        except TypeError:
            d[str(v)] = k
    return d


print(make_dict(x='Hello', y=[1, 2]))

print('\n' + '#' * 100 + '\n')


def return_matrix(m: list = None) -> None | list:
    "Напишите функцию для транспонирования матрицы"
    if m is None or len(m) == 0:
        return None

    num_rows = len(m)
    num_cols = len(m[0])
    t_matrix = []
    for i in range(num_cols):
        new_row = []
        for j in range(num_rows):
            new_row.append(m[j][i])
        t_matrix.append(new_row)
    return t_matrix


#  сначала пришлось узнать что вообще такое транспонирования матрица
#  потом эту задачу не мог представить в голове, как перевернуть, это типа елочки.
#  долго сидишь и подбираешь, если воображения не хватает.
#  цикл подсмотрел в яндексе, ну остальное дописал и оформил.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for i in return_matrix(matrix):
    print(i)
