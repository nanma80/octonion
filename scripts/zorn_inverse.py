from zorn import *
import marshal

inverse = dict()
unit_zorn = Zorn([[1, [0, 0, 0]], [[0, 0, 0], 1]])

for zorn in all_zorns:
  for inv_zorn in all_zorns:
    if zorn * inv_zorn == unit_zorn:
      if inv_zorn * zorn == unit_zorn:
        inverse[zorn] = inv_zorn
        continue
      else:
        print "Unexpected. Left inv != right inv", zorn, inv_zorn
        exit


for orbit_index in xrange(5):
  inv_orbits = dict()
  for key in inverse:
    inv_key = inverse[key]
    if key.orbit() == orbit_index:
      print str(key) + ' -> ' + str(inv_key)
      inv_orbit = inv_key.orbit()
      if inv_orbit in inv_orbits:
        inv_orbits[inv_orbit] += 1
      else:
        inv_orbits[inv_orbit] = 1
  print inv_orbits
  print




