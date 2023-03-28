import numdifftools as nd
import numpy as np
import itertools
import sympy


def F(x):
    x_1 = x[0]
    x_2 = x[1]
    return 10 * x_1 ** 2 + x_2 ** 2


def Fp(f, x):
    return f.subs('tk', x)


def paul(f, x_1 = 1, delta_x = 1, e_1 = 0.003, e_2 = 0.03):
    n_val = 0
    step = 2

    while (True):
        if step != 6:
            x_2 = x_1 + delta_x
            f_1, f_2 = Fp(f, x_1), Fp(f, x_2)
            if f_1 > f_2:
                x_3 = x_1 + 2 * delta_x
            else:
                x_3 = x_1 - delta_x
            f_3 = Fp(f, x_3)
            n_val += 3
        f_min = min([f_1, f_2, f_3])
        if f_min == f_1:
            x_min = x_1
        elif f_min == f_2:
            x_min = x_2
        elif f_min == f_3:
            x_min = x_3
        znam = ((x_2 - x_3) * f_1 + (x_3 - x_1) * f_2 + (x_1 - x_2) * f_3)
        if znam == 0:
            x_1 = x_min
            continue
        x_ = 1/2 * (
            ((x_2 ** 2 - x_3 ** 2) * f_1 + (x_3 ** 2 - x_1 ** 2) *
            f_2 + (x_1 ** 2 - x_2 ** 2) * f_3) /
            znam
        )
        f_ = Fp(f, x_)  
        n_val += 1
        first_module = abs((f_min - f_) / f_)
        second_module = abs((x_min - x_) / x_)
        if first_module < e_1 and second_module < e_2:
            x_star = x_
            step = 2
            break
        elif x_1 <= x_ <= x_3:

            step = 6

            if x_2 < x_:
                x_1 = x_2
            elif x_2 >= x_:
                x_3 = x_2
            x_2 = x_
            f_1, f_2, f_3 = Fp(f, x_1), Fp(f, x_2), Fp(f, x_3)
            n_val += 3
        else:
            x_1 = x_
            step = 2
    return x_star, n_val


def quick_gradient_fall(x_0 = [[0.5, 1]], e = 0.1, e_1 = 0.1, e_2 = 0.15, M = 10):
    N = 0
    step = 0
    t = [0]
    while True:

        if step != 3:
            k = 0
        grad = nd.Gradient(F)(np.array(x_0[k], dtype=np.float64))
        norm = np.linalg.norm(np.array(grad))
        if norm < e_1:
            x_res = x_0[k]
            break
        if k >= M:
            x_res = x_0[k]
            break
        tk = sympy.symbols('tk')
        try:
            x_0[k + 1] = (np.array(x_0[k]) - tk * np.array(grad))
        except IndexError:
            x_0.append(np.array(x_0[k]) - tk * np.array(grad))
        f = 2*x_0[k+1][0]**2 + x_0[k+1][0] * x_0[k+1][1] + 3 * x_0[k+1][1]**2
        try:
            t[k], _ = paul(f)
        except:
            a, _ = paul(f)
            t.append(a)
        f_k_1 = F(x_0[k+1])
        f_k = F(x_0[k])
        N += 2
        x_0[k + 1][0] = x_0[k + 1][0].subs('tk', t[k])
        x_0[k + 1][1] = x_0[k + 1][1].subs('tk', t[k])
        x_0[k + 1] = list(x_0[k + 1])
        norm_x = np.linalg.norm(np.array(x_0[k+1], dtype=np.float64) - np.array(x_0[k], dtype=np.float64))
        abs_f_x = abs(F(x_0[k+1]) - F(x_0[k]))
        norm_x_1 = np.linalg.norm(np.array(x_0[k], dtype=np.float64) - np.array(x_0[k-1], dtype=np.float64))
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
    x, N = quick_gradient_fall(x_0 = x_0, e = e, e_1 = e_1, e_2 = e_2, M = M)
    f_x = F(x)
    print(f"Минимум алгоритма в x = {x}, f(x) = {f_x}\nКоличество операций: {N}\nОтклонение +-{abs(true_f_x - f_x)}\n")
    