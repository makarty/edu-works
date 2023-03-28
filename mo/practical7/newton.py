import sympy
import numdifftools as nd
import numpy as np
import itertools

from scipy.optimize import fmin

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
        x_ = 1/2 * (                        # step 7
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


def F(x):
    x_1 = x[0]
    x_2 = x[1]
    return 7 * (x_2 - 1) ** 2 + (x_1 - 2) ** 2 # 0 (2, 1)

def matr(x_0):
    x_1 = x_0[0]
    x_2 = x_0[1]
    x1 = sympy.Symbol('x1')
    x2 = sympy.Symbol('x2')
    y = 5*x1**2+x2**2 - 2*x1-4*x2
    xx = y.diff(x1).diff(x1)
    xy = y.diff(x1).diff(x2)
    yx = y.diff(x2).diff(x1)
    yy = y.diff(x2).diff(x2)
    return xx.subs(x1, x_1), xy.subs([(x1, x_1),(x2, x_2)]), yx.subs([(x1, x_1),(x2, x_2)]), yy.subs(x2, x_2)


def gradient_fall(x_0 = [[0.5, 1]], e_1 = 0.1, e_2 = 0.15, M = 10):
    k = 0
    step = 0
    t = [1]
    N = 0
    while True:
        if step != 7:
            grad = nd.Gradient(F)(x_0[k])
            norm = np.linalg.norm(np.array(grad))
            if norm < e_1:
                x_res = x_0[k]
                break
            if k >= M:
                x_res = x_0[k]
                break
            H_x = np.array([[0,0],[0,0]])
            H_x[0][0], H_x[0][1], H_x[1][0], H_x[1][1] = matr(x_0[k])
            H_x_1 = np.linalg.inv(H_x)
            if np.all(np.linalg.eigvals(H_x_1) > 0):
                v = np.array([[grad[0]], [grad[1]]])
                d_k = - np.matrix(H_x_1) * np.matrix(v)
                d_k = np.array(d_k)
                d_k = np.array([round(d_k[0][0], 9), round(d_k[1][0], 9)])
                try:
                    t[k] = 1
                except:
                    t.append(1)
            else:
                d_k = - grad
            try:
                x_0[k+1] = x_0[k] + t[k]*d_k
            except:
                x_0.append(x_0[k] + t[k]*d_k)
            f_k_1 = F(x_0[k+1])
            f_k = F(x_0[k])
            N += 2
            try:
                if d_k == -1 * grad and not f_k_1 - f_k <= 0:
                    t[k] = t[k] / 2
            except:
                pass
            norm_x = np.linalg.norm(np.array(x_0[k+1], dtype=np.float64) - np.array(x_0[k], dtype=np.float64))
            abs_f_x = abs(f_k_1 - f_k)
            norm_x_1 = np.linalg.norm(np.array(x_0[k], dtype=np.float64) - np.array(x_0[k-1], dtype=np.float64))
            abs_f_x_1 = abs(f_k - F(x_0[k-1]))
            N += 1
            if norm_x < e_2 and abs_f_x < e_2 and abs_f_x_1 < e_2 and norm_x_1 < e_2:
                x_res = x_0[k+1]
                break
            else:
                k += 1
                step = 3
    return x_res, N


true_x = (2, 1)
true_f_x = 0

x = [[[0.5, 1]], [[50, 100]]]
e1 = [0.1, 0.9]
e2 = [0.15, 0.9]
m = [10, 2]

for x_0, e_1, e_2, M in itertools.product(x, e1, e2, m):
    print(f"Истинный минимум в x = {true_x}, f(x) = {true_f_x}")
    print(f"При параметрах x_0 = {x_0}, e_1 = {e_1}, e_2 = {e_2}, M = {M}")
    x, N = gradient_fall(x_0 = x_0, e_1 = e_1, e_2 = e_2, M = M)
    f_x = F(x)
    print(f"Минимум алгоритма в x = {x}, f(x) = {f_x}\nКоличество операций: {N}\nОтклонение +-{abs(true_f_x - f_x)}\n")
