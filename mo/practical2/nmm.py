# Вариант 11

import itertools
import numpy as np
from math import sqrt
from scipy.optimize import fmin


def f(x):
    return 7 * (x[1] - 1) ** 2 + (x[0] - 2) ** 2


print(fmin(f,np.array([0, 0])))

print("Таким образом, истинный минимум функции находится в точке (2, 1)\n")

point_min = [2, 1]
func_min = 0


def Nelder_Meade_method(alpha=1, beta=0.5, gamma=2, epsilon=0.1):
    x1 = (6, 6)
    x2 = (-2, -2)
    x3 = (5, 4)
    k = 0
    while True:
        f_dict = {x1: f(x1), x2: f(x2), x3: f(x3)}
        points_sorted = sorted(f_dict.items(), key=lambda x: x[1])
        xl = points_sorted[0][0]
        xh = points_sorted[len(points_sorted) - 1][0]
        xs = points_sorted[len(points_sorted) - 2][0]

        x4 = ((xl[0] + xs[0]) / 2, (xl[1] + xs[1]) / 2)

        algsum = 0
        for x in [x1, x2, x3]:
            algsum += (f(x) - f(x4)) ** 2
        algsum /= 3
        sigma = sqrt(algsum)
        if sigma <= epsilon:
            return xl, k
        k += 1
        x5 = list()
        for i in range(2):
            x5.append(x4[i] + alpha * (x4[i] - xh[i]))
        x5 = tuple(x5)

        if f(x5) <= f(xl):
            x6 = list()
            for i in range(2):
                x6.append(x4[i] + gamma * (x5[i] - x4[i]))
            x6 = tuple(x6)
            if f(x6) < f(xl):
                xh = x6
            else:
                xh = x5
            x1, x2, x3 = xl, xs, xh
        elif f(xs) < f(x5) <= f(xh):
            x7 = list()
            for i in range(2):
                x7.append(x4[i] + beta * (xh[i] - x4[i]))
            x7 = tuple(x7)
            xh = x7
            x1, x2, x3 = xl, xs, xh
        elif f(xl) < f(x5) <= f(xs):
            xh = x5
            x1, x2, x3 = xl, xs, xh
        elif f(x5) > f(xh):
            x_list = [x1, x2, x3]
            new_list = []
            for x in x_list:
                point = []
                for i in range(2):
                    point.append(round(xl[i] + 0.5 * (x[i] - xl[i]), 5))
                point = tuple(point)
                new_list.append(point)
            x1, x2, x3 = new_list


def main():
    print(f"Истинный минимум функции - {func_min} в точке {point_min}\n")
    alphas = [0.5, 1]
    betas = [0.25, 0.5]
    gammas = [1, 2]
    epsilons = [0.001, 0.01, 0.1]
    for alpha, beta, gamma, epsilon in itertools.product(alphas, betas, gammas, epsilons):
        print(f"При параметрах alpha = {alpha}, beta = {beta}, gamma = {gamma} и epsilon = {epsilon}")
        res, speed = Nelder_Meade_method(alpha, beta, gamma, epsilon)
        func_res = f(res)
        print(f"Минимум функции - {func_res} в точке {res}")
        print(f"Посчитан за {speed} операций")
        print(f"Отличие от истинного значения - {func_res - func_min}\n")


main()


