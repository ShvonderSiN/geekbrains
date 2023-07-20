# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from task_3 import Person


class Employee(Person):
    """Класс работника"""
    DIVIDER = 7

    def __init__(self, id_: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__id = id_
        self.__level = self.__calc_level()

    def __calc_level(self) -> int:
        sum_id = sum(map(int, str(self.__id)))
        return sum_id % Employee.DIVIDER

    def show_level(self) -> int:
        return self.__level

    def __repr__(self):
        return f'Объект {self.name}'


if __name__ == '__main__':
    valeriy = Employee(5555, name='Valeriy', age=40)
    print(valeriy.name, valeriy.show_level())
    print(valeriy)
