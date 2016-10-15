from pyglet.gl import *
from vectors import Vector

class Shape(object):
	def __init__(self, points, color = Vector(), scale = 1.0, glShape = GL_QUADS, glPolygonMode = GL_FILL):
		# a list of points to draw.  Stored as a vector.
		self.points = points
		# the color of the shape.  Stored as a vector.
		self.color = color
		# optionally increase/decrease the size of the shape.
		self.scale = scale
		# the shape mode passed to OpenGL when drawing points.
		self.glShape = glShape
		# the polygon mode controls if the shape is displayed as polygons, lines or vertices.
		self.glPolygonMode = glPolygonMode

	def retime(self, time):
		pass

	def draw(self):
		glPolygonMode(GL_FRONT_AND_BACK, self.glPolygonMode);

		glBegin(self.glShape)

		glColor3ub(self.color.x, self.color.y, self.color.z)

		for point in self.points:
			scaledPoint = point * self.scale
			glVertex3f(scaledPoint.x, scaledPoint.y, scaledPoint.z)

		glEnd()		

class Point(Shape):
	def __init__(self, p, color, pointSize=4):
		super(Point, self).__init__([p], color, glShape = GL_POINTS)
		self.pointSize = pointSize
		self.point = p

	def draw(self):
		glPointSize(self.pointSize)
		super(Point, self).draw()

class Line(Shape):
	def __init__(self, start, end, color):
		super(Line, self).__init__(
			[start, end],
			color,
			glShape = GL_LINES
		)
		self.start = start
		self.end = end

class Cube(Shape):
	def __init__(self, start, end, color):
		x = Vector(end.x - start.x, 0, 0)
		y = Vector(0, end.y - start.y, 0)
		z = Vector(0, 0, end.z - start.z)
		points = [
			start, start + x,
			start, start + y,
			start + y, start + x + y,
			start + x, start + x + y,
			start + z, start + x + z,
			start + z, start + y + z,
			start + y + z, start + x + y + z,
			start + x + z, start + x + y + z,
			start, start + z,
			start + x, start + x + z,
			start + y, start + y + z,
			start + x + y, start + x + y + z
		]
		super(Cube, self).__init__(
			points,
			color,
			glShape = GL_LINES,
			glPolygonMode = GL_LINE
		)
		self.start = start
		self.end = end