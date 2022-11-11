import numpy as np


def average_colour(image):
    """
    Функция получения среднего цвета из данной картики(То что мы будем рисовать)
    :param image: картинка (PIL obj)
    :return:
    """
    # Переводим картинку в массив пикселей точек данных.
    image_arr = np.asarray(image)
    # Уравниваем значение сначала по изображению, после по оси
    avg_color_per_row = np.average(image_arr, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return int(avg_color[0]), int(avg_color[1]), int(avg_color[2])


def weighted_average(hist) -> int:
    """
    Функция получения средневзвешенного значения(То что будет считать программа)
    :param hist: Гистограмма цвета квадранта
    :return:
    """
    total = sum(hist)
    error = 0

    if total > 0:
        value = sum(i * x for i, x in enumerate(hist)) / total
        error = sum(x * (value - i) ** 2 for i, x in enumerate(hist)) / total
        error = error ** 0.5

    return error


def get_transition(hist) -> float:
    """
    Фукнция для получения текущего порога перехода
    :param hist: Гистограмма цвета каждого пикселя квадранта
    :return:
    """
    red_transition = weighted_average(hist[:256])
    green_transition = weighted_average(hist[256:512])
    blue_transition = weighted_average(hist[512:768])

    # Переводим в чернобелый чтоб проще считать
    white_black_transition = red_transition * 0.2989 + green_transition * 0.5870 + blue_transition * 0.1140

    return white_black_transition
