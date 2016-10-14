import scipy.integrate as integrate
from vectors import Vector	# needed to represent vectors


# default function, returns 0.  Used for any unused axis.
NoFunction = lambda v, t:0

# f is a function in which to wrap constraints.
# constraints is a list of functions that demand specific conditions
# from a position and time variable.  If they are not met, then f
# returns default (which by default is 0).
# If there are no constraints, it just returns the origional function f.
def constraintWrapper( f, constraints, default=0 ):
	if len(constraints) > 0:
		def g(*args, **kwargs):
			for constraint in constraints:
				if not constraint(*args, **kwargs):
					return default
			return f(*args, **kwargs)
		g.f = f
		g.constraints = constraints
		g.default = default
		return g
	else:
		f.f = f
		f.constraints = constraints
		f.default = default
		return f


# this closure function takes in the three optional parameters of the u, v and w functions.
# u = function for the x value of the returned vector
# v = function for the y value of the returned vector
# w = function for the z value of the returned vector
# constraints = a list of functions that are evaluated to ensure that a given position and time are valid and can be evaluated
# each vector field function has these functions as attributes to be accessed individually.
def VectorField( u=NoFunction, v=NoFunction, w=NoFunction ):

	# This function is returned as customized by the u, v and w arguments.
	# It first evaluates each constraint with pos and t.  If they do not meet all constraints,
	# the function returns a (0, 0, 0) vector.
	# It creates a new vector calculated from the functions that represents a given field (velocity, acceleration, etc)
	# at position pos and at the optional time t.
	# t (time) defaults to 0.
	def FieldFunction( pos, t = 0 ):
		return Vector(
				u(pos, t),
				v(pos, t),
				w(pos, t),
			)
	FieldFunction.u = u
	FieldFunction.v = v
	FieldFunction.w = w

	return FieldFunction


# add in the del operators (gradiant, curl, divergence, etc.)
