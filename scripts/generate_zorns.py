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



generators = get_generators()

elements = generate_loop(generators)

print "Final element count:", len(elements)

print_elements(elements)
