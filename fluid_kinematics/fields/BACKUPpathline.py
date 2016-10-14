import numpy
from scipy.misc import derivative
from scipy.integrate import odeint

from vectors import Vector
from fields import VectorField



# f is a function that should take in a vector (position) and a float (time)
# dim is the dimension that this function is operating on (u is in the x dimension, or 0th dimenion)
# odeintWrapper wraps f in a function that takes in an array [x,y,z], and then converts it to a vector
# to be used by f.  It then places the result of f in an array [x,y,z] where the result is the dimension
# of the function
def odeintWrapper(f, dim):
	def c(a, t):
		v = [0, 0, 0]
		v[dim] = f(Vector(*a), t)
		return v
	return c

# V is a velocity field
# pInitial is the initial position of the particle
# Pathline returns a function that gives the position at any time of pInitial
def Pathline(V, pInitial):

	def applyOdeint(f, times, dim):
		# easier to make this a function than to write it three times.  f is the function (u, v, w)
		# times is the set of times to pass to odeint, and dim is the operating dimension of f.
		# it wraps f into an odeint compatable function, passes it in along with pInitial and times, and
		# then unwraps the value corresponding to the last time value and given dimension.
		return odeint( odeintWrapper(f, dim), pInitial.asArray(), times ).tolist()[-1][dim]
		o = odeint( odeintWrapper(f, dim), pInitial.asArray(), times )
		print(o)
		return o.tolist()[-1][dim]


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
		x = applyOdeint( V.u, times, 0 )
		y = applyOdeint( V.v, times, 1 )
		z = applyOdeint( V.w, times, 2 )
		return Vector(x, y, z)
	P.V = V
	P.point = pInitial
	return P
