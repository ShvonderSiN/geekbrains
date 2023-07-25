# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.

class Factorial:
    """Класс для вычисления факториала"""

    def __init__(self, k):
        self.k = k
        self._k_list = []

    def __call__(self, n) -> int:
        result = 1
        for n in range(1, n + 1):
            result *= n
        self._k_list.append(result)
        if len(self._k_list) > self.k:
            self._k_list.pop(0)
        return result

    def show_factorials(self):
        print(self._k_list)


if __name__ == '__main__':
    pass
    # todo сделать
