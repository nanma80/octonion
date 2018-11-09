from zorn import *

e1 = [1, 0, 0]
e2 = [0, 1, 0]
e3 = [0, 0, 1]

i = Zorn([[0, e3], [e3, 0]])
j = Zorn([[0, e2], [e2, 0]])
h = Zorn([[1, [0, 1, 0]], [[1, 0, 1], 1]])
print(i.det())
print(j.det())
print(h.det())

k = i * j
print "k:", k

e = ((j * h) * (h * i)) * (k * h)
print 'e:', e

print 'jh:', (j * h)

