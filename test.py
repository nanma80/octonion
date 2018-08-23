import numpy as np
from CayleyDickson import *

bases = []
for index in xrange(8):
  base = np.zeros(8)
  base[index] = 1
  bases.append(base)

identity = bases[0]

print multiply(bases[1], bases[2]), bases[3]
print multiply(bases[1], bases[4]), bases[5]
print multiply(bases[2], bases[4]), bases[6]
print multiply(bases[3], bases[4]), bases[7]
print bases[0]

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
