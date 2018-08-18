import numpy as np
from CayleyDickson import *

def get_generators():
  bases = []
  for index in xrange(8):
    base = np.zeros(8)
    base[index] = 1
    bases.append(base)

  identity = bases[0]

  h = np.zeros(8)
  for index in xrange(1, 5):
    h[index] = 1.0 / 2

  return [bases[1], bases[2], h]
  # return [bases[1], bases[2], bases[4]]

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
  generation_start_count = len(elements)
  for generator in generators:
    new_elements = [multiply(element, generator) for element in elements] + \
                   [multiply(generator, element) for element in elements]
    elements = join(elements, new_elements)
  print "Generation #" + repr(generation_index), ": ", len(elements)
  generation_end_count = len(elements)
  if generation_end_count == generation_start_count:
    break

print "Element count:", len(elements)
elements = sorted(elements, key=lambda vector: np.inner(vector, [10**(-n) for n in xrange(8)]))
for element in elements:
  print element

# for element in elements:
#   if abs(element[3]) < 0.0001 and abs(element[4]) < 0.0001 and abs(element[5]) < 0.0001 and abs(element[7]) < 0.0001:
#     print element

# max_inner = 100
# count = 0
# for element in elements:
#   inner = np.inner(element, elements[1])
#   if abs(inner - 0.5) < 0.001:
#     count += 1

# print count


# when generators are [bases[1], bases[2], h]
# 240 elements, 421 polytope. 56 nearest neighbors for each point
# 16 elements with (+/-1, 0, 0,...)
# 224 other elements. 16 of them in a group. 14 groups depending on the nonzero positions

