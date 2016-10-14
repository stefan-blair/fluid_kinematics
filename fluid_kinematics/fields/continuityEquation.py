from scipy.integrate import quad
from fields import partialDerivative
from vectors import Vector


# V = a vector field representing velocity with one "unknown function".
# unknown = an integer representing the function that is unknown.  0 is u, 1 is v, and 2 is w.
# this closure function will calculate and return a function that is the solution function to the unknown function.
def continuityEquation(V, unknown):
	fields = [V.u, V.v, V.w]
	dimensions = [0,1,2]
	dimensions.pop(unknown)

	# dimensions contains a list of known dimensions, while fields contains a list of the three velocity field functions.
	# solution uses continuity equation to calculate the solution by integrating with respect to the unknown dimension
	# a function that subtracts the partial derivatives of the known functions.
	def solution(p, t):
		createVector = lambda v: Vector(*(p[:unknown] + [v] + p[unknown+1:]))
		partials = lambda v: sum([-partialDerivative(fields[d], d, p[d], createVector(v), t) for d in dimensions])
		return quad(partials, 0, p[unknown])[0]

	return solution
