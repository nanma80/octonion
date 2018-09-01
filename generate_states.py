import numpy as np
import marshal
from CayleyDickson import *
from state import *

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

def tuplize(nparray):
  return tuple([int(c) for c in nparray])


def times(original, generator):
  vector = multiply(original, generator) / 2
  return tuplize(vector)


def generate_loop(generators, generation_limit = 10):
  elements = set([g for g in generators])

  for generation_index in xrange(generation_limit):
    generation_start_count = len(elements)
    for generator in generators:
      new_elements = [element * generator for element in elements]
      new_elements.extend([generator * element for element in elements])
      for el in new_elements:
        elements.add(el)
    print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  return elements

generators = [State(g) for g in get_generators()]
elements = generate_loop(generators)

print "Element count:", len(elements)


elements = [e.value for e in elements]

file_name = 'data/states_240.txt'

with open(file_name, 'w') as f:
  print marshal.dump(elements, f)

with open(file_name, 'r') as f:
  print marshal.load(f)
