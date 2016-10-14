import shapely.geometry as geometry
from scipy.spatial import ConvexHull

from vectors import Vector
from graphics import Shape


# shape is a very simple shape, a set of at least 4 points.
# point is a coordinate that is tested to be contained in shape.
def raycast2D(shape, point):
	# The algorithm creates two lists of points.
	# The first list contains the points in shape.  The second contains
	# the first list, plus point.

	points1 = map(lambda v:(v.x,v.y), shape.points)

	# ensure that there are at least 4 unique coordinates
	if len(set(points1)) < 4:
		return False

	points2 = points1 + [(point.x,point.y)]

	# Two convex hulls are created around these two lists, and compared for
	# equality.  If they are the same, then the the point is inside the shape.
	# If it was outside, it would have created a different convex hull.

	hull1 = ConvexHull(points1)
	hull2 = ConvexHull(points2)

	return hull1.vertices.tolist() == hull2.vertices.tolist()


# shapes are an array of polygons that make up a larger, 3D polygon.
# point is the point to check.  (If it is within the 3D shape or not)
def raycast3D(shapes, point):

	def convert(p, d):
		# p is a vector, d is a dimension (0=x, 1=y, 2=z)
		# Remove dimension d from vector p, and then convert p to (x,y)
		return Vector(*(p[:d]+p[d+1:]))


	# for each dimension x,y,z, check each shape in shapes
	# to see if it contains point.  In order for point to be
	# contained in the 3D polygon described by shapes, it must
	# be contained in at least one of the flattened shapes.
	# If there is a dimension without a match, the point IS NOT
	# contained in shapes.  Otherwise, it is contained in shapes.

	for d in xrange(3):
		match = False
		point2D = convert(point, d)

		for shape in shapes:
			points = map(lambda v: convert(v,d), shape.points)
			if raycast2D( Shape(points), point2D ):
				match = True
				break
		if not match:
			return False

	return True
