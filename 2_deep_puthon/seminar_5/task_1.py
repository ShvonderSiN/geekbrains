# Задание №1
# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
#  хранятся в кортеже как значения второго ключа.

try:
    string = '1/43/555/12/90/125/98'.split('/')
    # string = input('Enter string: ').strip().split('/')
    key1, key2 = string[1].strip(), string[2].strip()
    d = {}
    d[key1], _, _, *d[key2] = string
    print(d)
except ValueError:
    print('Введите корректную строку')


