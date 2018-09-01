import numpy as np
from CayleyDickson import *


class State(object):
  """2 times the actual octonion"""

  def __init__(self, value):
    self.value = value
    self.value = self.tuplize()

  def tuplize(self):
    return tuple([int(c) for c in self.value])

  def __mul__(self, other):
    vector = State(multiply(self.value, other.value) / 2)
    return vector

  def __rmul__(self, other):
    vector = State(multiply(other.value, self.value) / 2)
    return vector

  def __str__(self):
    if sum([abs(el) for el in self.value]) == 4:
      return str(self.value) + '/2'
    else:
      return str(State([c/2 for c in self.value]).tuplize())
