# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст

class Person:
    """Класс человека"""

    def __init__(self, name: str, f_name: str = None, age: int = 0):
        self.__age = age
        self.name = name
        self.f_name = f_name

    def show_age(self) -> int:
        """Возвращает текущий возраст"""
        return self.__age

    def birthday(self) -> None:
        """Добавляет возраст"""
        self.__age += 1

    def full_name(self) -> str:
        """Возвращает ФИО"""
        return f'{self.name} {self.f_name}'


if __name__ == '__main__':
    petya = Person('Peter', "Ivanov", 15)
    print(petya.name, petya.show_age())
    petya.birthday()
    print(petya.name, petya.show_age())
