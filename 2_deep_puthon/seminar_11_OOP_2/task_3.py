# Задание №3
# Добавьте к задачам 1 и 2 строки документации для классов.


if __name__ == '__main__':
    from task_1 import MyString
    from task_2 import Archive

    print(MyString.__doc__, "#" * 100, sep='\n')
    help(Archive)
