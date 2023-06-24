def dabble_detector(x: list) -> list:
    """Дан список повторяющихся элементов.
    Вернуть список с дублирующимися элементами.
    В результирующем списке не должно быть дубликатов.
    Пример:
    [1, 2, 3, 1, 2, 4, 5] -> [1, 2]"""

    lst_dub = []
    try:
        for _ in x:
            el = x.pop(0)
            if el in x:
                lst_dub.append(el)
    except IndexError:
        return []
    return lst_dub


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


def word_count(string: str, num_words: int = 10) -> dict:
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


if '__main__' == __name__:
    lst = [1, 2, 3, 1, 2, 4, 5]
    print(lst, '->', dabble_detector(lst))

    for k, v in word_count(STRING, 5).items():
        print(f'Слово "{k}" встречается {v} раз')
