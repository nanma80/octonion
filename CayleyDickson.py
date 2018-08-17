# by John Cook
# https://www.johndcook.com/blog/2018/07/10/cayley-dickson/
import numpy as np

def conj(x):
    xstar = -x
    xstar[0] *= -1
    return xstar 

def CayleyDickson(x, y):
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
