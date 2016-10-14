from scipy.misc import derivative
from fields import VectorField
from fields import partialDerivative
from vectors import Vector



def materialDerivativeComponent( field, f ):
	def s( pos, t=0 ):
		dt = partialDerivative( f, 3, t, pos, t )
		dx = field.u(pos,t) * partialDerivative( f, 0, pos.x, pos, t )
		dy = field.v(pos,t) * partialDerivative( f, 1, pos.y, pos, t )
		dz = field.w(pos,t) * partialDerivative( f, 2, pos.z, pos, t )

		return dt + dx + dy + dz
	return s

def materialDerivative( field ):

	u = materialDerivativeComponent( field, field.u )
	v = materialDerivativeComponent( field, field.v )
	w = materialDerivativeComponent( field, field.w )

	return VectorField( u=u, v=v, w=w )
