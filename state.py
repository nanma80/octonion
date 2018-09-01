import numpy as np
from CayleyDickson import *


class State(object):
  def __init__(self, value, from_double=False):
    self.value = np.array(value)
    if from_double:
      self.value = self.value / 2.0
    self.double = tuple([int(round(2 * c)) for c in self.value])

  def tuplize(self):
    return tuple([int(c) for c in self.value])

  def __mul__(self, other):
    vector = State(multiply(self.value, other.value))
    return vector

  def __rmul__(self, other):
    vector = State(multiply(other.value, self.value))
    return vector

  def __str__(self):
    has_half_integer = any(el % 2 == 1 for el in self.double)

    if has_half_integer:
      return str(self.double) + '/2'
    else:
      return str(tuple([c / 2 for c in self.double]))

  def __hash__(self):
    return hash(self.double)

  def __eq__(self, other):
    return self.double == other.double

