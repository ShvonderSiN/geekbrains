# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


if __name__ == '__main__':
    from sem7_package.tools import writer, names_generator

    for _ in range(10):
        name = names_generator()
        writer('names.txt', name, append=True)
