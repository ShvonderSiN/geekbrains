# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.

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
        if len(self._k_list) >= self.k:
            self._k_list.pop(0)
        return result

    def show_factorials(self) -> None:
        print(self._k_list)


if __name__ == '__main__':
    f = Factorial(3)
    print(f'{f(5)}')
    print(f'{f(3)}')
    print(f'{f(4)}')
    print(f'{f(7)}')
    f.show_factorials()
