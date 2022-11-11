"""Модуль с поиском расстояния Левенштейна"""


def lev_dist(string_1, string_2):
    """
    Расстояние Левенштейна
    :param string_1: первая строка
    :type string_1: str
    :param string_2: вторая строка
    :type string_2: str
    :return: количество операций, чтобы получить вторую строку из первой
    """
    interval = {}
    for i in range(-1, len(string_1) + 1):
        interval[(i, -1)] = i + 1
    for i in range(-1, len(string_2) + 1):
        interval[(-1, i)] = i + 1
    for i in range(len(string_1)):
        for j in range(len(string_2)):
            inter = 0
            first_delete, insert_second = interval[(i - 1, j)] + 1, interval[(i, j - 1)] + 1
            if string_1[i] != string_2[j]:
                inter = 1
            replace = interval[(i - 1, j - 1)] + inter
            interval[(i, j)] = min(first_delete, insert_second, replace)

    return interval[len(string_1) - 1, len(string_2) - 1]


def search_substring(string_original, sub_string, mistake=1):
    """
    Функция для поиска подстроки
    :param string_original: строка
    :type string_original: str
    :param sub_string: подстрока
    :type sub_string: str
    :param mistake: количетсво ошибок
    :type mistake: int
    :return: словарь с индексом и подстрокой
    """
    dict_string = {}
    if len(string_original) == len(sub_string):
        first_sub = string_original[:len(sub_string)]
    else:
        first_sub = string_original[:len(sub_string) - mistake]
    last_sub = len(string_original) - len(sub_string) + mistake
    last = string_original[last_sub:]
    if (lev_dist(first_sub, sub_string) <= mistake) and (len(string_original) - len(sub_string) not in dict_string):
        dict_string[0] = first_sub
    for i in range(last_sub):
        string_temp = string_original[i:i + len(sub_string)]
        interval = lev_dist(string_temp, sub_string)
        if string_temp[0] == ' ' and interval == mistake + 1:
            interval -= 1
        print(f'количество операций {interval}')
        if (interval <= mistake) and (len(string_original) - len(sub_string) not in dict_string):
            if len(string_temp) == len(sub_string):
                dict_string[i] = string_temp
    if lev_dist(last, sub_string) <= mistake and (len(string_original) - len(sub_string) not in dict_string):
        dict_string[last_sub] = last
    return dict_string
