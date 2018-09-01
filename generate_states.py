import numpy as np
import marshal
from CayleyDickson import *
from state import *

use_quaternions = False
# use_quaternions = True


def get_generators():
  bases = []
  for index in xrange(8):
    base = np.zeros(8)
    base[index] = 1
    bases.append(base)

  identity = bases[0]

  h = np.array([0, 1, 1, 1, 1, 0, 0, 0]) / 2.0
  if use_quaternions:
    h = np.array([1, 1, 1, 1, 0, 0, 0, 0]) / 2.0 # to generate Hurwitz quaternions

  return [bases[1], bases[2], h]
  # return [bases[1], bases[2], bases[4]]

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


element_values = [e.double for e in elements]

file_name = 'data/states_' + str(len(elements))+ '.txt'

with open(file_name, 'w') as f:
  print marshal.dump(element_values, f)
