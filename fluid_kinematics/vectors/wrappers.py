from vector import Vector

def integralWrapper( f ):	# takes in x,y,z,t values and fills them in to make a new vector
	def wrapper( *vals ):
		return f( Vector( *vals ) )
	return wrapper
