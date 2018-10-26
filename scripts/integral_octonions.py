import numpy as np
import random
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
  h3 = [1, 1, 1, 1, 0, 0, 0, 0]
  omega = [1, 1, 1, 0, 1, 0, 0, 0]
  psi = [0, 1, 1, 1, 0, 1, 0, 0]
  balanced = [1, 1, 1, 1, 0, 0, 0, 0]
  balanced2 = [1, 1, 0, 0, 1, 1, 0, 0]

  return [bases[1], bases[2], h]
  # return [bases[1], omega, psi]
  # return [bases[1], bases[2], psi]
  # return [bases[1], balanced, balanced2]
  # return [bases[1], bases[2], h3]
  # return [bases[1], bases[2], bases[4]]

def norm(octonion):
  return np.sqrt(multiply(conj(octonion), octonion)[0]) / 2

def tuplize(nparray):
  return tuple([int(c) for c in nparray])


def times(original, generator):
  vector = multiply(original, generator) / 2
  return tuplize(vector)


def generate_loop(generators, generation_limit = 10):
  elements = set([tuplize(g) for g in generators])

  for generation_index in xrange(generation_limit):
    generation_start_count = len(elements)
    for generator in generators:
      new_elements = []
      new_elements.extend([times(element, generator) for element in elements]) # right multiply
      new_elements.extend([times(generator, element) for element in elements]) # left multiply
      for el in new_elements:
        elements.add(el)
    print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  return elements

def plot(elements, generators):
  import networkx as nx
  import matplotlib.pyplot as plt

  graph = nx.Graph()
  graph.add_nodes_from(elements)
  edges = []
  colors = ['red', 'green', 'blue', 'magenta']
  for g_index in xrange(len(generators)):
    generator = generators[g_index]
    edge_per_color = []
    for element in elements:
      edge_per_color.append((element, times(element, generator)))
    graph.add_edges_from(edge_per_color)
    edges.append(edge_per_color)

  pos = nx.spring_layout(graph)
  nx.draw_networkx_nodes(graph, pos, node_color='black')
  for index in xrange(len(edges)):
    nx.draw_networkx_edges(graph, pos, edgelist=edges[index], edge_color=colors[index], arrows=True)
  plt.show()

generators = get_generators()
elements = generate_loop(generators)

print "Element count:", len(elements)


elements = list(elements)
random_indices = [random.randrange(len(elements)) for index in xrange(3)]

a, b, c = [elements[index] for index in random_indices]

print "random_indices: ", random_indices

print "Associativity. Can be False:", times(times(a, b), c) == times(a, times(b, c))
print "Associator ==", times(times(times(a, b), c), conj(times(a, times(b, c))))

print "Moufang properties. Should be all True"
print times(c, times(a, times(c, b))) == times(times(times(c, a), c), b)
print times(a, times(c, times(b, c))) == times(times(times(a, c), b), c)
print times(times(c, a), times(b, c)) == times(times(c, times(a, b)), c)
print times(times(c, a), times(b, c)) == times(c, times(times(a, b), c))

# plot(elements, generators)

# for element in elements:
  # print element
#   norm_element = norm(element)
#   if norm_element < 0.99 or norm_element > 1.01:
#     print element, norm_element

all_indices = set()

for element in elements:
  if sum([abs(el) for el in element]) == 4:
    indices = []
    for index, coordinate in enumerate(element):
      if coordinate != 0:
        indices.append(index)
    all_indices.add(tuple(indices))

all_indices = sorted(list(all_indices))
print "Indices of nonzero half int vectors in elements are:"
for indices in all_indices:
  print indices

# for element in elements:
#   if sum(element) == 4:
#     indices = []
#     for index, coordinate in enumerate(element):
#       if coordinate != 0:
#         indices.append(index)
#     print element, indices





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
