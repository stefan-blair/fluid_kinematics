import math

class Vector:

	def __init__(self, x=0, y=0, z=0):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return str( (self.x, self.y, self.z) )

	# overloaded addition/subtraction vector operators.  Adds/subtracts components seperately
	def __add__(self, b):
		return Vector( self.x + b.x, self.y + b.y, self.z + b.z )

	def __iadd__(self, b):
		self.x += b.x
		self.y += b.y
		self.z += b.z
		return self

	def __sub__(self, b):
		return Vector( self.x - b.x, self.y - b.y, self.z - b.z )
	def __isub__(self, b):
		self.x -= b.x
		self.y -= b.y
		self.z -= b.z
		return self

	def __div__(self, b):
		# b must be a scalar
		return Vector( self.x / b, self.y / b, self.z / b )
	def __idiv__(self, b):
		# b must be a scalar
		self.x /= b
		self.y /= b
		self.z /= b
		return self

	def __mul__(self, b):
		# b must be a scalar
		return Vector( self.x * b, self.y * b, self.z * b )
	def __imul__(self, b):
		# b must be a scalar
		self.x *= b
		self.y *= b
		self.z *= b
		return self

	def __abs__(self):
		return Vector( abs(self.x), abs(self.y), abs(self.z) )

	def __eq__(self, other):
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __getitem__(self, key):
		return self.asArray()[key]

	def __setitem__(self, key, value):
		values = self.asArray()
		values[key] = values
		self.x, self.y, self.z = values
	def __delitem__(self, key):
		self[key] = 0

	# returns the vector dot product between the calling vector and vector b
	def dot(self, b):
		return self.x * b.x + self.y * b.y + self.z * b.z
	# returns the vector cross product between the calling vector and vector b
	def cross(self, b):
		return Vector(	self.y * b.z - self.z * b.y,
				self.z * b.x - self.x * b.z,
				self.x * b.y - self.y * b.x	)

	def magnitude(self):
		return math.sqrt( self.x**2 + self.y**2 + self.z**2 )

	# returns the vector components as an array
	def asArray(self):
		return [self.x, self.y, self.z]
	# returns the vector components as a tuple
	def asTuple(self):
		return (self.x, self.y, self.z)

	# get the components as vectors with 0 for the other components
	def xHat(self):
		return Vector( self.x, 0, 0 )
	def yHat(self):
		return Vector( 0, self.y, 0 )
	def zHat(self):
		return Vector( 0, 0, self.z )

	def withoutDimension(self,d):
		c = self.asArray()
		c[d] = 0
		return Vector(*c)

	# get a replica of the vector in order to pass by value or avoid modifying the origional copy
	def copy(self):
		return Vector(*self.asArray())
