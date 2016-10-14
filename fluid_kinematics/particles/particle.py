from vectors import Vector
from fields import VelocityField, PositionField, AccelerationField


# this class describes a particle, including all data required to accurately describe its position and motion.

EmptyField = lambda v: 0

class Particle:
	def __init__(self, initialPosition, velocity = EmptyField, acceleration = EmptyField):
		# initialPos = initial position of the particle.
		# velocity = velocity field in which the particle resides.
		# acceleration = acceleration field in which the particle resides.
		self.initialPosition = initialPosition
		self.velocity = velocity
		self.acceleration = acceleration

	def position( t = 0 ):
#		for i in xrange(t):
