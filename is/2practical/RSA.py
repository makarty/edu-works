import random
import sympy
from math import log2, ceil


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x


def RSA(Q, P):
    global s, e
    # print(Q, P)
    N = Q * P
    fn = (Q - 1) * (P - 1)
    flag = True
    while flag:
        s = random.randint(1, fn)
        # print(f"s: {s}")
        if fn % s != 0 and sympy.isprime(s):
            flag = False

    gcd, x, y = extended_gcd(s, fn)
    e = fn + x
    return N, s, round(e)


def encrypt(string, N, s):
    print(f"N - {N, s}")
    lst = []
    lst_coding = []
    if len(string) % 2 != 0:
        string = string + chr(0)
    for i in range(0, len(string) - 1, 2):
        tmp = string[i] + string[i + 1]
        b = int.from_bytes(bytes(tmp, "utf-8"), "little")
        lst.append(b)
    for i in lst:
        c = round(pow(i, s, N))
        lst_coding.append(str(c))
    return lst_coding


def decrypt(lst_coding, N, e):
    lst = []
    for i in lst_coding:
        t = round(pow(int(i), e, N))
        t = t.to_bytes(ceil(log2(t) / 8), "little")
        lst.append(str(t, "utf-8"))
    print(f'lst - {lst}')
    return lst


def rand47():
    k = 0
    lst_PQ = []
    flag = True
    while flag:
        PQ = random.randint(100000000000000000000000,
                            309999999999999999999999)
        if sympy.isprime(PQ):
            lst_PQ.append(PQ)
            k += 1
            if k == 2:
                return lst_PQ
        else:
            pass
