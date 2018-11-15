from zorn import *


def get_generators():
  field_q = 2
  e1 = [1, 0, 0]
  e2 = [0, 1, 0]
  e3 = [0, 0, 1]

  i = Zorn([[0, e3], [e3, 0]], field_q)
  j = Zorn([[0, e2], [e2, 0]], field_q)
  h = Zorn([[1, [0, 1, 0]], [[1, 0, 1], 1]], field_q)

  return [i, j, h]

def generate_loop(generators, generation_limit = 10):
  elements = set([g for g in generators])

  for generation_index in xrange(generation_limit):
    generation_start_count = len(elements)
    for generator in generators:
      new_elements = []
      new_elements.extend([element * generator for element in elements])
      new_elements.extend([generator * element for element in elements])
      for el in new_elements:
        elements.add(el)
    print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  return elements

generators = get_generators()

elements = generate_loop(generators)

print "Final element count:", len(elements)

for element in elements:
  print element

# counts = [0, 0]
# for index in xrange(2 ** 8):
#   binary = [int(c) for c in list(bin(index + 2 ** 8)[3:])]
#   candidate = Zorn([[binary[0], [binary[1], binary[2], binary[3]]], [[binary[4], binary[5], binary[6]], binary[7]]])
#   counts[candidate.det()] += 1
# print counts # 136 zorn matrices with det == 0, 120 with det == 1. Elements are all those with det == 1



