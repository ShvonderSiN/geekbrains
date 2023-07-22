# Задание №5
# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Animal:
    """Животное: базовый класс"""

    def __init__(self, name, age=0, can_fly: bool = True):
        self.name = name
        self.__age = age
        self.can_fly = can_fly

    def show_age(self):
        return self.__age

    def show_can_fly(self):
        return self.can_fly


class Bird(Animal):
    """Животное птица"""

    def __init__(self, wings: int = 2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wings = wings

    def show_num_of_wings(self):
        return self.wings


class Fish(Animal):
    """Животное рыба"""

    def __init__(self, num_fin: int = 2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_fin = num_fin

    def show_num_fin(self):
        return self.num_fin


if __name__ == '__main__':
    fish = Fish(name='Барракуда', age=3, num_fin=7, can_fly=False)
    bird = Bird(name='Колли бри', age=1, wings=2, can_fly=True)
    fly = 'летает' if fish.can_fly else 'не летает'
    print(f"{fish.name} это рыба, возрастом {fish.show_age()} года, у нее "
          f"{fish.show_num_fin()} плавников и конечно она {'летает' if fish.can_fly else 'не летает'}")
    print(f"{fish.name} это птица, возрастом {fish.show_age()} лет, у нее "
          f"и конечно она {'летает' if fish.can_fly else 'не летает'}")
