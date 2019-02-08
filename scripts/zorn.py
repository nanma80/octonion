import marshal

dict_element_orbit = dict()
all_zorns = []

file_name = './data/zorn_orbit_120.txt'
with open(file_name, 'r') as f:
  marshalled_dict = marshal.load(f)

def dot(a, b, field_q):
  return (a[0] * b[0] + a[1] * b[1] + a[2] * b[2]) % field_q


def cross(a, b, field_q):
  return [
    (a[1] * b[2] - a[2] * b[1]) % field_q,
    (a[2] * b[0] - a[0] * b[2]) % field_q,
    (a[0] * b[1] - a[1] * b[0]) % field_q
  ]


def scaler_multiply(s, vector, field_q):
  return [(s * element) % field_q for element in vector]


def multiply(z1, z2, field_q):
  new_a = (z1.a * z2.a + dot(z1.alpha, z2.beta, field_q)) % field_q
  new_b = (z1.b * z2.b + dot(z1.beta, z2.alpha, field_q)) % field_q
  new_alpha_list = [
    scaler_multiply(z1.a, z2.alpha, field_q), 
    scaler_multiply(z2.b, z1.alpha, field_q), 
    scaler_multiply(-1, cross(z1.beta, z2.beta, field_q), field_q)
  ]
  new_alpha = map(lambda x:sum(x) % field_q, zip(*new_alpha_list))
  new_beta_list = [
    scaler_multiply(z2.a, z1.beta, field_q), 
    scaler_multiply(z1.b, z2.beta, field_q), 
    cross(z1.alpha, z2.alpha, field_q)
  ]
  new_beta = map(lambda x:sum(x) % field_q, zip(*new_beta_list))
  return Zorn([[new_a, new_alpha], [new_beta, new_b]])


class Zorn(object):
  def __init__(self, matrix, field_q = 2):
    self.field_q = field_q
    self.matrix = matrix
    self.a = self.matrix[0][0]
    self.b = self.matrix[1][1]
    self.alpha = self.matrix[0][1]
    self.beta = self.matrix[1][0]


  def det(self):
    return (self.a * self.b - dot(self.alpha, self.beta, self.field_q)) % self.field_q


  def sequence(self):
    return [self.a] + [self.b] + self.alpha + self.beta


  def orbit(self):
    return dict_element_orbit[self]
    
  def __mul__(self, other):
    return multiply(self, other, self.field_q)


  def __rmul__(self, other):
    return multiply(other, self, self.field_q)


  def __str__(self):
    # return 'matrix = ' + str(self.matrix) + ', det = ' + str(self.det())
    return str(self.matrix) + ', orbit ' + str(self.orbit())


  def __hash__(self):
    # return hash(self.a) + hash(self.b)
    return hash(tuple(self.sequence()))


  def __eq__(self, other):
    return self.matrix == other.matrix

for key in marshalled_dict:
  orbit_number = marshalled_dict[key]
  zorn = Zorn([[key[0], [key[2], key[3], key[4]]], [[key[5], key[6], key[7]], key[1]]])
  dict_element_orbit[zorn] = orbit_number
  all_zorns.append(zorn)

