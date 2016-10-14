import numpy
from scipy.misc import derivative
from scipy.integrate import odeint

from vectors import Vector
from fields import VectorField



# V is a velocity field
# odeintWrapper wraps V's components in a function that takes in an array [x,y,z], and then converts it to a vector
# to be used by each component.  It then evaluates each velocity component at position a, time t, to find the next position.
# This is returned as an array for use by odeint.
def odeintWrapper(V):
	def c(a, t):
		return [f(Vector(*a),t) for f in [V.u, V.v, V.w]]
	return c

# V is a velocity field
# pInitial is the initial position of the particle
# Pathline returns a function that gives the position at any time of pInitial
def Pathline(V, pInitial):

	# this function takes in t, a given time at which to calculate pInitial's new time
	# a is an optional accuracy value (the accuracy of the generated times table).
	def P(t, a = 50):
		# if t == 0, no time has passed.  if a == 0, there is no accuracy.
		if t == 0 or a == 0:
			return pInitial
		# generate times values from 0 to t
		times = numpy.linspace(0, t, a)
		# use scipy's odeint (ordinary differential equation integral) function to
		# calculate each dimensional value of the new Vector
		x, y, z = odeint( odeintWrapper(V), pInitial.asArray(), times).tolist()[-1]
		return Vector(x, y, z)
	P.V = V
	P.point = pInitial
	return P
