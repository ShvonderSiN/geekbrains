# Решить задачи, которые не успели решить на семинаре.
# ✔ Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# ✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


if __name__ == '__main__':
    from sem7_package.tools import file_renamer

    file_renamer(old_ext='py',
                 new_ext='.png',
                 new_file_name='newFilename_',
                 range_=(1, 3),
                 dir_='../',
                 prefix_num=3)
