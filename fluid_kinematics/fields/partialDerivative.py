from scipy.misc import derivative
from vectors import Vector


# returns a function that takes a single argument
# and returns the partial derivative of f with respect to respect
# at position pos, where pos.respect = the single argument.
def partialDerivative( f, respect, v, pos, t=0 ):
	def g(r):
		x, y, z = pos.asArray()
		args = [x, y, z, t]
		args[respect] = r
		return f( Vector( *args[:3] ), args[3] )
	return derivative(g, v)
