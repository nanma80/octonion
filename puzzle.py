import numpy as np
import random
import marshal
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

  return [bases[1], bases[2], h, bases[0]]


def tuplize(nparray):
  return tuple([int(c) for c in nparray])


def times(original, generator):
  vector = multiply(original, generator) / 2
  return tuplize(vector)


def load_states():
  state_file_name = 'data/states_240.txt'
  with open(state_file_name, 'r') as f:
    states = marshal.load(f)
    return states


def pretty_print(state):
  if sum([abs(el) for el in state]) == 4:
    return str(state) + '/2'
  else:
    return str(tuplize([c/2 for c in state]))

def main():
  i, j, h, winning_state = [tuplize(c) for c in get_generators()]
  states = load_states()
  states_set = set(states)

  print "Loaded " + repr(len(states)) + " states"

  current_state = states[random.randrange(len(states))]

  print "Current state: " + pretty_print(current_state)
  prompt_string = \
  """Enter an expression to right-multiply to the current state. 
  Use i, j, or h as basic operations
  Use times(expression1, expression2) to construct complex expressions.
  Example: times(i, times(j, h))
  The objective is to create """ + pretty_print(winning_state) + """
  Enter q to stop.
  """

  print(prompt_string)

  print "Current state: " + pretty_print(current_state)

  while True:
    input_string = raw_input("Input = ")

    if input_string == 'q':
      break

    try:
      input_value = eval(input_string)
      if input_value not in states_set:
        print "Input value " + repr(input_value) + " is not a valid state"
        raise
      print "Input is: " + repr(input_value)
      current_state = times(current_state, input_value)
      print "Current state = Current state * Input. New current state: " + pretty_print(current_state)

      if current_state == winning_state:
        print "You win!"
        break

    except Exception as err:
      print "Invalid input"
      print prompt_string
      print "Current state: " + pretty_print(current_state)


if __name__ == '__main__':
  main()


