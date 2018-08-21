import numpy as np
from CayleyDickson import *

def get_generators():
  bases = []
  for index in xrange(8):
    base = np.zeros(8)
    base[index] = 2 # double the numbers so that half int becomes int
    bases.append(base)

  identity = bases[0]

  h = [0, 1, 1, 1, 1, 0, 0, 0]
  # h2 = [0, 1, 1, 1, 0, 0, 1, 0]

  return [bases[1], bases[2], h]
  # return [bases[1], bases[2], bases[4]]

def norm(octonion):
  return np.sqrt(multiply(conj(octonion), octonion)[0]) / 2

def tuplize(nparray):
  return tuple([int(c) for c in nparray])


def generation_function(original, generator):
  vector = multiply(original, generator) / 2
  return tuplize(vector)


def generate_loop(generators, generation_limit = 10):
  elements = set([tuplize(g) for g in generators])

  for generation_index in xrange(generation_limit):
    generation_start_count = len(elements)
    for generator in generators:
      new_elements = [generation_function(element, generator) for element in elements] + \
                     [generation_function(generator, element) for element in elements]
      for el in new_elements:
        elements.add(el)
    print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  return elements

generators = get_generators()
elements = generate_loop(generators)

print "Element count:", len(elements)

# for element in elements:
#   norm_element = norm(element)
#   if norm_element < 0.99 or norm_element > 1.01:
#     print element, norm_element


for element in elements:
  if sum(element) == 4:
    indices = []
    for index, coordinate in enumerate(element):
      if coordinate != 0:
        indices.append(index)
    print element, indices

# when generators are [bases[1], bases[2], h]
# 240 elements, 421 polytope. 56 nearest neighbors for each point
# 16 elements with (+/-1, 0, 0,...)
# 224 other elements. 16 of them in a group. 14 groups depending on the nonzero positions

# http://math.ucr.edu/home/baez/week194.html
# These integral domains are also discussed
# in Coxeter's paper Regular and Semi-Regular Polyotpes III
# (Math. Z. 200, 3-45, 1988), where he describes the 240 units
# of an E8 integral domain as
# "... the 16 + 16 + 16 octaves
# +/-1, +/-i, +/-j, +/-k, +/-e, +/-ie, +/-je, +/-ke,
# (+/-1 +/-ie +/-je +/-ke)/2,
# (+/-e +/-i  +/-j  +/-k )/2,
# and the 192 others derived from the last two expressions by
# cyclically permuting the 7 symbols [ i,j,k,e,ie,je,ke ]
# in the peculiar order
#      e, i, j, ie, ke, k, je
# ...
# It seems somewhat paradoxical ... that the cyclic permutation
#     ( e, i, j, ie, ke, k, je ),
# which preserves the integral domain
# (and the finite projective [Fano] plane ...)
# is not an automorphism of the whole ring of octaves;
# it transforms the associative triad ijk
# into the anti-associative triad j ie je.
# On the other hand, the permutation
#     ( e ie je i k ke j ),
# which IS an automorphism of the whole ring of octaves
# (and of the finite [Fano] plane ...)
# transforms this particular integral domain into another
# one of R. H. Bruck's cyclic of seven such domains.  ...".
