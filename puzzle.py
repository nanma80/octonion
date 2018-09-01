#!/usr/bin/env python

import numpy as np
import random
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

  return [bases[1], bases[2], h, bases[0]]


def load_states():
  state_file_name = 'data/states_240.txt'
  if use_quaternions:
    state_file_name = 'data/states_24.txt'
  with open(state_file_name, 'r') as f:
    states = marshal.load(f)
    return [State(s, True) for s in states]


def main():
  i, j, h, winning_state = [State(c) for c in get_generators()]
  states = load_states()
  states_set = set(states)

  print "Loaded " + repr(len(states)) + " states"

  current_state = states[random.randrange(len(states))]

  print "Random initial state: " + str(current_state)
  help_string = \
    """
      Enter an input expression to right-multiply to the current state.
      With the convention in https://en.wikipedia.org/wiki/Octonion#Definition
      and the abbreviations:
      i = """ + str(i) + """
      j = """ + str(j) + """
      h = """ + str(h) + """
      Use i, j, or h as generators and use ( ) and octonion multiplication *
      to construct complex expressions.
      Example: h * (i * j)
      The objective is to create """ + str(winning_state) + """
      Enter q to stop.
    """

  winning_message = \
  """
     __      __                         __       __  __            __ 
    /  \    /  |                       /  |  _  /  |/  |          /  |
    $$  \  /$$/______   __    __       $$ | / \ $$ |$$/  _______  $$ |
     $$  \/$$//      \ /  |  /  |      $$ |/$  \$$ |/  |/       \ $$ |
      $$  $$//$$$$$$  |$$ |  $$ |      $$ /$$$  $$ |$$ |$$$$$$$  |$$ |
       $$$$/ $$ |  $$ |$$ |  $$ |      $$ $$/$$ $$ |$$ |$$ |  $$ |$$/ 
        $$ | $$ \__$$ |$$ \__$$ |      $$$$/  $$$$ |$$ |$$ |  $$ | __ 
        $$ | $$    $$/ $$    $$/       $$$/    $$$ |$$ |$$ |  $$ |/  |
        $$/   $$$$$$/   $$$$$$/        $$/      $$/ $$/ $$/   $$/ $$/ 
  """


  print(help_string)

  print "Current state: " + str(current_state)

  while True:
    input_string = raw_input("Input = ")

    if input_string in ['q', 'exit']:
      break

    try:
      input_value = eval(input_string)
      if input_value not in states_set:
        print "Input value " + str(input_value) + " is not a valid state"
        raise

      print "Input = " + input_string + " = " + str(input_value)
      current_state = current_state * input_value
      print "New state = Current state * Input = " + str(current_state)

      if current_state == winning_state:
        print winning_message
        break

    except Exception:
      print "Invalid input"
      print help_string
      print "Current state: " + str(current_state)


if __name__ == '__main__':
  main()
