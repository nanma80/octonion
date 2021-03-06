from zorn import *
import marshal

# file_name = './data/zorn_orbit_120.txt'
# with open(file_name, 'r') as f:
#   marshalled_dict = marshal.load(f)

# dict_element_orbit = dict()
# for key in marshalled_dict:
#   orbit_number = marshalled_dict[key]
#   zorn = Zorn([[key[0], [key[2], key[3], key[4]]], [[key[5], key[6], key[7]], key[1]]])
#   dict_element_orbit[zorn] = orbit_number

# print dict_element_orbit

e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 1]

i = Zorn([[0, e3], [e3, 0]])
j = Zorn([[0, e2], [e2, 0]])
h = Zorn([[1, [0, 1, 0]], [[1, 0, 1], 1]])
# print(i.det())
# print(j.det())
# print(h.det())

# k = i * j
# print "k:", k

# e = ((j * h) * (h * i)) * (k * h)
# print 'e:', e

# print 'jh:', (j * h)

mix1 = (i * j) * h # (12)(34) -> 1(23)4 swap middle => 2413. orbit3
mix2 = i * (j * h) # 2134 (12)34 -> 1(234) => ??? 2413*. orbit 4
mix3 = i * (h * j) # 2134 (12)34 -> 1(234) => ??? 2341*. orbit 0
mix2inv = (h * i) * j # 3142. orbit 3
mix3inv = (j * h) * i # 4123. orbit 3

print mix1 # orbit 3
print mix1 * mix1 # orbit 4
print mix1 * mix1 * mix1 # mix1^3 = 1 not ^4; orbit 3
print

print mix2 # orbit 4
print mix2 * mix2 # orbit 3. What permutation is it? inv(mix2) == (h * i) * j
print mix2 * mix2 * mix2 # mix2^3 = 1 not ^4; orbit 3
print

print mix2 * mix2 == mix2inv # 1324 -> 3124 -> 3142
print mix2inv * mix2 # 1
print mix2 * mix2inv # 1
print

print mix3 # orbit 0
print mix3 * mix3 # orbit 3. What permutation is it? inv(mix3) == ?
print mix3 * mix3 * mix3 # mix2^3 = 1 not ^4; orbit 3
print

print mix3 * mix3 == mix3inv
print mix3inv * mix3
print mix3 * mix3inv
print

# print j * h
# print (j * h) * (j * h)
# print j * h * j * h # same as above. Moufang loop: two generators: always associative
# print (j * h) * (j * h) * (j * h)
# print j * h * j * h * j * h # same as above. Moufang loop: two generators: always associative

# print i * j * h * i * j * h * j * h * i * j * h * j # identity
