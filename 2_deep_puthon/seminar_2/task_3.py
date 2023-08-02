"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions."""
from __future__ import annotations

from fractions import Fraction
from typing import Optional, Tuple


def calculate_fractions(f1, f2) -> tuple[Fraction, Fraction] | None:
    try:
        frac1 = Fraction(f1)
        frac2 = Fraction(f2)

        summ = frac1 + frac2
        product = frac1 * frac2

        return summ, product
    except (ValueError, ZeroDivisionError):
        return None


fraction1 = input("Введите первую дробь (в формате a/b): ")
fraction2 = input("Введите вторую дробь (в формате a/b): ")

result = calculate_fractions(fraction1, fraction2)
if result:
    sum_fraction, product_fraction = result
    print("Сумма дробей:", sum_fraction)
    print("Произведение дробей:", product_fraction)
else:
    print("Некорректный ввод.")
