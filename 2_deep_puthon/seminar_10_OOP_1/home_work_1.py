# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали.
# Превратите функции в методы класса. Задачи должны решаться через вызов методов экземпляра.
# Например:
# 1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
# суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
# 2. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# 3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
from random import randint


class RandomTasks:
    """ Сборная солянка"""
    _TRIALS = 10
    _LOWER_LIMIT = 0
    _UPPER_LIMIT = 1000

    def task_triangle(self, a, b, c) -> None:
        """
        Задача на треугольник
        """
        if a + b > c and a + c > b and b + c > a:
            print("Треугольник существует")

            if a == b and b == c:
                print("Треугольник равносторонний")
            elif a == b or b == c or a == c:
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")
        else:
            print("Треугольник не существует")

    def guessing(self) -> None:
        """
        ✔ Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
    должна подсказывать «больше» или «меньше» после каждой попытки.
        """
        num = randint(self._LOWER_LIMIT, self._UPPER_LIMIT + 1)

        while self._TRIALS > 0:
            try:
                ges_num = float(input('Введи число: '))
            except ValueError:
                print('Принимаются только цифры')
                continue

            if ges_num > num:
                print('Бери ниже')
            elif ges_num < num:
                print('Бери выше')
            elif ges_num == num:
                print('Угадал!')
                break
            self._TRIALS -= 1
            print(f'Осталось {self._TRIALS} попыток')
        else:
            print('Попытки кончились')

    def word_count(self, string: str, num_words: int = 10) -> dict:
        """ Сначала выделил все слова в нижнем регистре и добавил в список,
        затем вернул словарь с встречающимися словами
        string: Входящая строка
        num_word: количество отобранных слов, не обязательный
        """
        string = string.split()
        new_string = []

        for word in string:
            new_word = ''.join(i for i in word if i.isalnum())
            new_string.append(new_word.lower())
        del string

        result_dict = {}
        for word in new_string:
            count = new_string.count(word)
            if word not in result_dict:
                result_dict[word] = count
        return {k: v for k, v in sorted(result_dict.items(), key=lambda x: x[1])[:-num_words - 1:-1]}


if __name__ == '__main__':
    tasks = RandomTasks()

    tasks.task_triangle(3, 2, 5)

    STRING = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed pulvinar elit vel mauris blandit consectetur. Nullam sed lorem lorem, sed pulvinar pulvinar metus. 
    Etiam et lectus lectus, sit amet amet commodo. Vestibulum vestibulum, mauris 
    at at tristique tristique, risus risus lacinia lacinia, metus metus mauris. 
    In in euismod euismod aliquam aliquam vel. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed sed massa massa, ut ullamcorper ullamcorper sapien. Phasellus phasellus 
    imperdiet imperdiet justo justo, vitae vitae pellentesque pellentesque metus metus euismod. 
    Etiam etiam commodo commodo risus risus, nec nec ullamcorper ullamcorper sapien. 
    Sed sed mi mi, a a bibendum bibendum ante ante vitae. 
    Duis duis id id diam diam, eu eu aliquam aliquam urna urna ac. 
    Vivamus vivamus vel vel odio odio, a a faucibus faucibus metus metus vel."""

    for k, v in tasks.word_count(STRING, 5).items():
        print(f'Слово "{k}" встречается {v} раз')
