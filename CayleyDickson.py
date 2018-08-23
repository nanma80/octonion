# by John Cook
# https://www.johndcook.com/blog/2018/07/10/cayley-dickson/
# index, bases[index]
# 0    , 1
# 1    , i
# 2    , j
# 3    , k
# 4    , e
# 5    , ie
# 6    , je
# 7    , ke
# This naming convention is consistent with https://en.wikipedia.org/wiki/Octonion#Definition
# But not with http://math.ucr.edu/home/baez/octonions/node3.html
# An easy way to tell is to check if e_1 * e_2 == e_3 or e_4

import numpy as np

def conj(x):
    x = np.array(x)
    xstar = -x
    xstar[0] *= -1
    return xstar 

def CayleyDickson(x, y):
    x, y = np.array(x), np.array(y)

    n = len(x)

    if n == 1:
        return x*y

    m = n // 2

    a, b = x[:m], x[m:]
    c, d = y[:m], y[m:]
    z = np.zeros(n)
    z[:m] = CayleyDickson(a, c) - CayleyDickson(conj(d), b)
    z[m:] = CayleyDickson(d, a) + CayleyDickson(b, conj(c))
    return z

def multiply(x, y):
    return CayleyDickson(x, y)
