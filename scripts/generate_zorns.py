import random
import marshal
from zorn import *


def get_generators():
  field_q = 2
  e1 = [1, 0, 0]
  e2 = [0, 1, 0]
  e3 = [0, 0, 1]

  i = Zorn([[0, e3], [e3, 0]], field_q)
  j = Zorn([[0, e2], [e2, 0]], field_q)
  h = Zorn([[1, [0, 1, 0]], [[1, 0, 1], 1]], field_q)

  g1 = Zorn([[1, e1], [e1, 0]], field_q)
  g2 = Zorn([[1, e2], [e2, 0]], field_q)
  g3 = Zorn([[0, e3], [e3, 1]], field_q)


  return [i, j, h]
  # return [g1, g2, g3]

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
    # print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  return elements


def generate_coset(seed, generators, generation_limit = 10):
  elements = set([seed])

  for generation_index in xrange(generation_limit):
    generation_start_count = len(elements)
    for generator in generators:
      new_elements = []
      new_elements.extend([element * generator for element in elements])
      for el in new_elements:
        elements.add(el)
    # print "Generation #" + repr(generation_index), ": ", len(elements)
    generation_end_count = len(elements)
    if generation_end_count == generation_start_count:
      break
  elements = sorted(list(elements), key=lambda x:x.sequence())
  return elements


def get_orbit_hash(coset):
  return hash(tuple(coset))

def print_elements(elements):
  unit_zorn = Zorn([[1, [0, 0, 0]], [[0, 0, 0], 1]])

  for element in elements:
    order = 0
    if element == unit_zorn:
      print "order = 1,", element
    elif (element * element) == unit_zorn:
      order = 2
      if element.a == element.b:
        print "order = 2,", element
      else:
        raise(Exception("unexpected order 2: " + str(element)))
    elif (element * element) * element == unit_zorn:
      order = 3
      if element.a == (element.b + 1) % 2:
        print "order = 3,", element
      else:
        raise(Exception("unexpected order 3: " + str(element)))
    else:
      raise(Exception("unexpected order > 3: " + str(element)))


def check_properties(elements):
  def times(a, b):
    return multiply(a, b, 2)

  elements = list(elements)
  random_indices = [random.randrange(len(elements)) for index in xrange(3)]

  a, b, c = [elements[index] for index in random_indices]

  print "random_indices: ", random_indices

  print "Associativity. Can be False or True:", times(times(a, b), c) == times(a, times(b, c))
  
  print "Moufang properties. Should be all True"
  print times(c, times(a, times(c, b))) == times(times(times(c, a), c), b)
  print times(a, times(c, times(b, c))) == times(times(times(a, c), b), c)
  print times(times(c, a), times(b, c)) == times(times(c, times(a, b)), c)
  print times(times(c, a), times(b, c)) == times(c, times(times(a, b), c))



generators = get_generators()

elements = list(generate_loop(generators))
print "Final element count:", len(elements)

orbit_hashes = set()

for index in xrange(len(elements)):
  coset = generate_coset(elements[index], generators)
  orbit_hashes.add(get_orbit_hash(coset))

orbit_hashes = sorted(list(orbit_hashes))
print orbit_hashes

dict_element_orbit = dict()

for index in xrange(len(elements)):
  coset = generate_coset(elements[index], generators)
  orbit_number = orbit_hashes.index(get_orbit_hash(coset))
  dict_element_orbit[tuple(elements[index].sequence())] = orbit_number

print dict_element_orbit

file_name = './data/zorn_orbit_' + str(len(elements))+ '.txt'

with open(file_name, 'w') as f:
  marshal.dump(dict_element_orbit, f)
  print "Saved states to " + file_name
  


# counts = [0, 0]
# for index in xrange(2 ** 8):
#   binary = [int(c) for c in list(bin(index + 2 ** 8)[3:])]
#   candidate = Zorn([[binary[0], [binary[1], binary[2], binary[3]]], [[binary[4], binary[5], binary[6]], binary[7]]])
#   counts[candidate.det()] += 1
# print counts # 136 zorn matrices with det == 0, 120 with det == 1. Elements are all those with det == 1


# print_elements(elements)
# check_properties(elements)

