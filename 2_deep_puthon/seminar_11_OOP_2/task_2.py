# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Класс Архив"""
    int_archive = []
    str_archive = []

    def __init__(self, number: int, string: str):
        self.number = number
        self.string = string
        Archive.int_archive.append(self.number)
        Archive.str_archive.append(self.string)

    def __repr__(self):
        return f'Archive({self.number}, {self.string})\n{self.int_archive}\n{self.str_archive}'


if __name__ == '__main__':
    a = Archive(5, 'Sergei')
    b = Archive(6, 'Vasya')
    print(b)
