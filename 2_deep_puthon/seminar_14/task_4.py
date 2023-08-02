# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)


from task_1_2 import alpha_string


def test_equal():
    assert 'hello world' == alpha_string('hello world')


def test_registr():
    assert 'hello world' == alpha_string('heLLo worLD')


def test_punctuation():
    assert 'hello world' == alpha_string('.Hello, 88World,')


def test_en_only():
    assert ' hello world ' == alpha_string('Здрасьте, Hello World Вася!8)))')


def test_all():
    assert ' hello world  ' == alpha_string('Здрасьте, Hello World Вася Мухин!8)))')


if __name__ == '__main__':
    pass
