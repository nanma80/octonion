import numpy as np
from CayleyDickson import *

def get_generators():
  zero = np.zeros(8)

  identity = zero.copy()
  identity[0] += 1

  e_1 = zero.copy()
  e_1[1] = 1

  e_2 = zero.copy()
  e_2[2] = 1

  e_4 = zero.copy()
  e_4[4] = 1


  h = zero.copy()
  h[1] = 1.0/2
  h[2] = 1.0/2
  h[4] = 1.0/2
  h[7] = 1.0/2

  # for index in xrange(1, 5):
  #   h[index] = 1.0 / 2

  return [e_1, e_2, h]

def join(original_list, new_list):
  for element in new_list:
    matched = False
    for old_element in original_list:
      if np.linalg.norm(old_element - element) < 10 ** (-10):
        matched = True
        break
    if not matched:
      original_list.append(element)
  return original_list


elements = get_generators()
print elements

generators = get_generators()

for generation_index in xrange(10):
  for generator in generators:
    new_elements = [multiply(element, generator) for element in elements]
    elements = join(elements, new_elements)
  print generation_index, len(elements)

print len(elements)


