"""Реализация муравьиного алгоритма"""
import random
from functools import wraps
from math import hypot
from time import time

import numpy as np
import pandas as pd


def timeit(func):
    """Функция подсчета времени работы функции."""

    @wraps(func)
    def modificated_func(*args, **kwargs):
        now = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"[RESULT]: Function '{func.__name__}' time is {end - now} sec.")
        return result

    return modificated_func


def euclidean_distance(first_city, second_city):
    """
    Функция подсчета евклидового расстояния между городами
    :param first_city: координаты первого города
    :type first_city: class city
    :param second_city: координаты второго города
    :param second_city: class city
    :return: евкливого расстояние между точками
    """

    return hypot(first_city.x - second_city.x, first_city.y - second_city.y)


def aspiration(pherom, proximity, alfa=1, beta=5):
    """
    Функция подсчета желания муравья идти по маршруту
    :param pherom: феромон(привлекательность пути для муравья)
    :type pherom:
    :param proximity: близость
    :type proximity:
    :param alfa: коэффициент важности феромона
    :type alfa: float
    :param beta: коэффициент важности близости
    :type beta: float
    :return:
    """
    return pherom ** alfa * proximity ** beta


def min_road(dist, roads):
    """
    Функция расчета минимального расстояния
    :param dist: массив расстояний
    :type dist: np.array
    :param roads: пути
    :return:
    """
    dist_min = dist.argmin()
    best_way = roads[dist_min]
    return dist[dist_min], best_way


def ant(cities, number_of_iter, min_dist=None, best_way=[]):
    """
    Функция итерации муравьиного алгоритма
    :param cities:список городов
    :type cities: list
    :param number_of_iter: количество проходов
    :type number_of_iter: int
    :param min_dist: минимальное расстояние
    :type min_dist: float
    :param best_way: лучший путь
    :type best_way: list
    :return: минимальное расстояние, лучший путь, дистанция, близость и феромоны
    """

    proximity, pherom = np.zeros((len(cities), len(cities)), dtype=np.float), \
                        np.zeros((len(cities), len(cities)), dtype=np.float)
    np.fill_diagonal(proximity, np.nan)
    np.fill_diagonal(pherom, np.nan)
    for row in range(len(cities)):
        for col in range(len(cities)):
            if row != col:
                proximity[row][col], pherom[row][col] = \
                    round(4 / euclidean_distance(cities[row], cities[col]), 2), 0.2

    for i in range(number_of_iter):
        min_dist, best_way, distances, proximity, pherom = algorithm(cities, min_dist, best_way, proximity,
                                                                     pherom)

    solution = pd.Series(distances)
    solution.to_csv("solution.csv")
    return min_dist, best_way


@timeit
def algorithm(cities, min_dist, best_road, proximity, pherom, num_ant=5):
    """
    Муравьиный алгоритм

    :param cities: список городов
    :type cities: list
    :param min_dist: Минимальное полученное расстояние
    :type min_dist: float
    :param best_road: лучший путь из пройденных муравьями
    :type best_road: list
    :param proximity: близость пуи
    :type proximity: list
    :param pherom: феромоны для муравьев
    :type pherom: list
    :param num_ant: количество муравьев
    :type num_ant: int
    :return: минимальное расстояние, лучший путь, дистанция, близость и феромоны
    """
    desire_array = np.zeros(len(cities), dtype=np.float)
    roads = np.zeros((num_ant, len(cities) + 1), dtype=np.int32)
    passed = np.zeros(len(cities), dtype=np.bool8)
    for iter in range(num_ant):
        index = random.randint(0, len(cities) - 1)
        passed.fill(False)
        road = roads[iter]
        road[0], road[-1] = index, index
        index_road = 1
        while passed.sum() != len(cities) - 1:
            passed[index], ind, prob = True, [], []
            for i in range(len(passed)):
                if not passed[i]:
                    ind.append(i)
            for i in range(len(ind)):
                desire_array[i] = aspiration(pherom[index][ind[i]], proximity[index][ind[i]])
            desire_sum = desire_array[:len(ind)].sum()
            for i in range(len(ind)):
                prob.append(desire_array[i] / desire_sum)
            index = random.choices(ind, weights=prob)[0]
            road[index_road] = index
            index_road += 1

    dist = np.zeros(num_ant, dtype=np.float)
    ind_distances = 0
    for road in roads:
        length = 0
        for i in range(len(road) - 1):
            length += euclidean_distance(cities[road[i]], cities[road[i + 1]])
        dist[ind_distances] = length
        ind_distances += 1

    if min_dist is None:
        min_dist, best_road = min_road(dist, roads)

    elif min(dist) < min_dist:
        min_dist, best_road = min_road(dist, roads)

    for i in range(len(dist)):
        number_of_pheromones = 3050 / dist[i]

        for j in range(len(roads[0]) - 1):
            ind_pher_row = roads[i][j]
            ind_pher_col = roads[i][j + 1]

            pherom[ind_pher_row][ind_pher_col] = pherom[ind_pher_row][ind_pher_col] + number_of_pheromones
            pherom[ind_pher_col][ind_pher_row] = pherom[ind_pher_col][ind_pher_row] + number_of_pheromones

    pherom2 = []

    for i in pherom:
        pherom2.append([])
        for j in i:
            if j is None:
                pherom2[-1].append(None)
            else:
                pherom2[-1].append(round(j * 0.7, 3))
    dist = []
    for i in range(len(best_road) - 1):
        dist.append([euclidean_distance(cities[best_road[i]], cities[best_road[i + 1]])])
    return min_dist, best_road, dist, proximity, pherom2
