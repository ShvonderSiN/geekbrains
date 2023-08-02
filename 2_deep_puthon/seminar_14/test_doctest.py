class Calculator:

    def __validator(self, a, b):
        if not all(isinstance(x, (int, float)) for x in (a, b)):
            raise TypeError('Вы должны пользоваться только числами')

    def add(self, a, b):
        """
        Сложение
        >>> calc = Calculator()
        >>> calc.add(5, 3)
        8
        >>> calc.add(-3, 4)
        1
        >>> calc.add('2', 4)
        Traceback (most recent call last):
        ...
        TypeError: Вы должны пользоваться только числами
        """
        self.__validator(a, b)
        return a + b

    def sub(self, a, b):
        self.__validator(a, b)
        return a - b

    def mul(self, a, b):
        self.__validator(a, b)
        return a * b

    def div(self, a, b):
        self.__validator(a, b)
        return a / b
