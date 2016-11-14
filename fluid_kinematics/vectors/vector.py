import math

class Vector:

	def __init__(self, x=0, y=0, z=0):
		# create x, y and z variables defaulting to 0
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		# overloaded so that if the vector is printed, show each component
		return str( (self.x, self.y, self.z) )

	def __add__(self, b):
		# overloaded addition operator.  return a new vector with each 
		# component as b's component added to self's component
		return Vector( self.x + b.x, self.y + b.y, self.z + b.z )

	def __iadd__(self, b):
		# overloaded addition assignment operator.  add each of b's components
		# to self's components
		self.x += b.x
		self.y += b.y
		self.z += b.z
		return self

	def __sub__(self, b):
		# overloaded subtraction operator.  return a new vector with each 
		# component as b's component subtracted from self's component
		return Vector( self.x - b.x, self.y - b.y, self.z - b.z )
	def __isub__(self, b):
		# overloaded subtraction assignment operator.  subtract each of b's 
		# components from self's components
		self.x -= b.x
		self.y -= b.y
		self.z -= b.z
		return self

	def __div__(self, b):
		# b must be a scalar.  return a new vector with each of self's
		# components divided by b
		return Vector( self.x / b, self.y / b, self.z / b )
	def __idiv__(self, b):
		# b must be a scalar.  divide each component by b
		self.x /= b
		self.y /= b
		self.z /= b
		return self

	def __mul__(self, b):
		# b must be a scalar.  return a new vector with each of self's
		# components multiplied by b
		return Vector( self.x * b, self.y * b, self.z * b )
	def __imul__(self, b):
		# b must be a scalar.  multiply each component by b
		self.x *= b
		self.y *= b
		self.z *= b
		return self

	def __abs__(self):
		# return a new vector with the absolute value of each of self's 
		# components
		return Vector( abs(self.x), abs(self.y), abs(self.z) )

	def __eq__(self, other):
		# for the two vectors to be equal, each component must be equal
		return self.x == other.x and self.y == other.y and self.z == other.z

	def __getitem__(self, key):
		# overloaded access [] operator so vector can be treated as a 3 element
		# array.  provide read access
		return self.asArray()[key]

	def __setitem__(self, key, value):
		# overloaded access[] operator so vector can be treated as a 3 element
		# array.  provide write access
		values = self.asArray()
		values[key] = values
		self.x, self.y, self.z = values
	def __delitem__(self, key):
		# set the given dimension to 0
		self[key] = 0

	def dot(self, b):
		# returns the vector dot product between the calling vector and vector 
		# b
		return self.x * b.x + self.y * b.y + self.z * b.z
	def cross(self, b):
		# returns the vector cross product between the calling vector and 
		# vector b
		return Vector(	self.y * b.z - self.z * b.y,
				self.z * b.x - self.x * b.z,
				self.x * b.y - self.y * b.x	)

	def magnitude(self):
		# returns the magnitude of the vector (square root of each dimension 
		# squared)
		return math.sqrt( self.x**2 + self.y**2 + self.z**2 )
	
	def asArray(self):
		# returns the vector components as an array
		return [self.x, self.y, self.z]

	def asTuple(self):
		# returns the vector components as a tuple
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

	def copy(self):
		# get a replica of the vector in order to pass by value or avoid 
		# modifying the original copy
		return Vector(*self.asArray())
