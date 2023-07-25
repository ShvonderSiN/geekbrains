# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.
import csv


class NameValidator:
    """Дескриптор проверяет переданное название предмета"""

    @classmethod
    def __name_validator(cls, value):
        if type(value) != str:
            raise ValueError('Должна быть строка')
        if not value.isalpha():
            raise ValueError('Допускаются только буквы')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.__name_validator(value)
        return setattr(instance, self.name, value.capitalize())


class Subject:
    """Дескриптор, хранит, валидирует и добавляет оценки и баллы"""

    def __init__(self, name):
        self.name = name
        self.marks = []
        self.scores = []

    def __set_name__(self, owner, name):
        self.name = '__' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        return setattr(instance, self.name, value)

    def __repr__(self):
        return f'marks({self.marks}), scores{self.scores}'

    def add_mark(self, value):
        if 2 <= value <= 5:
            self.marks.append(value)
        else:
            raise ValueError('Оценка должна быть от 2 до 5')

    def add_score(self, value):
        if 0 <= value <= 100:
            self.scores.append(value)
        else:
            raise ValueError('Оценка за тест должна быть от 0 до 100')


class Student:
    name = NameValidator()
    f_name = NameValidator()

    def __init__(self, name: str, f_name: str, subjects_file: str = 'subjects.csv'):
        self.name = name
        self.f_name = f_name
        self.__subjects = {}

        with open(subjects_file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            # next(reader)
            for row in reader:
                self.__subjects[row[0].capitalize()] = Subject(name=row[0])

    @property
    def subjects(self):
        return self.__subjects

    def average_marks(self, subject):
        return sum(self.subjects[subject].marks) / len(self.subjects[subject].marks)

    def average_all_subjects(self):
        all_marks = [mark for obj in self.subjects.values() for mark in obj.marks]
        return sum(all_marks) / len(all_marks)

    def average_scores(self, subject):
        return sum(self.subjects[subject].scores) / len(self.subjects[subject].scores)

    def add_mark(self, subject_name, mark):
        self.__subject_validator(subject_name)
        self.__subjects[subject_name].add_mark(mark)

    def add_score(self, subject_name, score):
        self.__subject_validator(subject_name)
        self.subjects[subject_name].add_score(score)

    def __repr__(self):
        return f'Student({self.name}, {self.f_name})'

    def __subject_validator(self, subject_name):
        if subject_name.capitalize() not in self.subjects.keys():
            raise ValueError('Такого предмета не существует')


if __name__ == '__main__':
    s = Student('vasya', 'Shekin')
    s.add_mark('Math', 4)
    s.add_score('Math', 53)
    s.add_mark('History', 3)
    s.add_score('History', 78)
    print(s)
    print(f'Средняя оценка по математике: {s.average_marks("Math")}')
    print(f'Средний балл по математике: {s.average_scores("Math")}')
    print(f'Средняя оценка по всем предметам: {s.average_all_subjects()}')
    print()

    print(*s.subjects.items(), sep='\n')

# output
# Student(Vasya, Shekin)
# Средняя оценка по математике: 4.0
# Средний балл по математике: 53.0
# Средняя оценка по всем предметам: 3.5
#
# ('Math', marks([4]), scores[53])
# ('Biology', marks([]), scores[])
# ('Chemistry', marks([]), scores[])
# ('Geography', marks([]), scores[])
# ('History', marks([3]), scores[78])
