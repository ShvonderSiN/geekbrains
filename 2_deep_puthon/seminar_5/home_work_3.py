# ✔ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
from typing import Generator


def fibonacci_generator(count: int = 10) -> Generator[int]: #  Так правильно или можно без импорта?
    a, b = 0, 1
    while count != 0:
        yield a
        a, b = b, a + b
        count -= 1


print(*fibonacci_generator(15))
