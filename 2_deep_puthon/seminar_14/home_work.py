# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.
import pytest


class Calculator:

    def __validator(self, a, b):
        if not all(isinstance(x, (int, float)) for x in (a, b)):
            raise TypeError('Вы должны пользоваться только числами')

    def add(self, a, b):
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
