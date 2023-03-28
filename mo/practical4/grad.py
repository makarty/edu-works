import numdifftools as nd
import numpy as np
import itertools


def F(x):
    x_1 = x[0]
    x_2 = x[1]
    return 10 * x_1 ** 2 + x_2 ** 2


def gradient_fall(x_0 = (0.5, 1), e = 0.1, e_1 = 0.1, e_2 = 0.15, M = 10):
    N = 0
    step = 0
    t = [0]
    while True:
        if step != 7:
            if step != 3:
                k = 0
            grad = nd.Gradient(F)(x_0[k])
            norm = np.linalg.norm(np.array(grad))
            if norm < e_1:
                x_res = x_0[k]
                break
            if k >= M:
                x_res = x_0[k]
                break
            try:
                if len(t) < 2:
                    t[k] = 0.5
                else:
                    t[k] = t[k-1]
            except:
                t.append(t[k-1])
        try:
            x_0[k + 1] = (np.array(x_0[k]) - t[k] * np.array(grad))
        except IndexError:
            x_0.append(np.array(x_0[k]) - t[k] * np.array(grad))
        f_k_1 = F(x_0[k+1])
        f_k = F(x_0[k])
        N += 2
        if f_k_1 - f_k < 0 or f_k_1 - f_k < -e * norm * norm: # or f_k_1 - f_k < -e * norm * norm
            step = 9
        else:
            t[k] = t[k]/2
            step = 7
            continue
        norm_x = np.linalg.norm(np.array(x_0[k+1]) - np.array(x_0[k]))
        abs_f_x = abs(F(x_0[k+1]) - F(x_0[k]))
        norm_x_1 = np.linalg.norm(np.array(x_0[k]) - np.array(x_0[k-1]))
        abs_f_x_1 = abs(F(x_0[k]) - F(x_0[k-1]))
        N += 4
        if norm_x < e_2 and abs_f_x < e_2 and abs_f_x_1 < e_2 and norm_x_1 < e_2:
            x_res = x_0[k+1]
            break
        else:
            k += 1
            step = 3
    return x_res, N


true_x = (0, 0)
true_f_x = 0

x = [[[0.5, 1]], [[20, 40]]]
e1 = [0.1, 0.00001]
e2 = [0.1, 0.9]
e3 = [0.15, 0.9]
m = [10, 2]

for x_0, e, e_1, e_2, M in itertools.product(x, e1, e2, e3, m):
    print(f"Истинный минимум в x = {true_x}, f(x) = {true_f_x}")
    print(f"При параметрах x_0 = {x_0}, e = {e}, e_1 = {e_1}, e_2 = {e_2}, M = {M}")
    x, N = gradient_fall(x_0 = x_0, e = e, e_1 = e_1, e_2 = e_2, M = M)
    f_x = F(x)
    print(f"Минимум алгоритма в x = {x}, f(x) = {f_x}\nКоличество операций: {N}\nОтклонение +-{abs(true_f_x - f_x)}\n")
