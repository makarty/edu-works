import random
import sympy


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
    for i in string:
        lst.append(ord(i))
    for i in lst:
        c = round(pow(i, s, N))
        lst_coding.append(str(c))
    return lst_coding


def decrypt(lst_coding, N, e):
    lst = []
    for i in lst_coding:
        t = round(pow(int(i), e, N))
        if t > 1114111:
            return ['E', 'R', 'R', 'O', 'R']
        lst.append(chr(t))
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
