# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.


class FactorialGenerator:
    """Генератор факториала"""

    def __init__(self, stop: int, start: int = 1, step: int = 1):
        self.start = start
        self.stop = stop
        self.step = step

    def __factorial(self, fact):
        current = 1
        for i in range(1, fact + 1):
            current *= i
        return current

    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.stop:
            raise StopIteration
        result = self.__factorial(self.start)
        self.start += self.step
        return result

    def __repr__(self):
        return f'{FactorialGenerator.__name__}({self.start = }, {self.stop = }, {self.step = })'


if __name__ == '__main__':
    f = FactorialGenerator(5)

    # for i in f:
    #     print(i)
    print(next(f))
    print(next(f))
    print(next(f))
