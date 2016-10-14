from pyglet.gl import *
from vectors import Vector

class Shape(object):
	def __init__(self, points, color = Vector(), scale = 1.0, glShape = GL_QUADS, glPolygonMode = GL_FILL):
		self.points = points			# a list of points to draw.  Stored as a vector.
		self.color = color			# the color of the shape.  Stored as a vector.
		self.scale = scale			# optionally increase/decrease the size of the shape.
		self.glShape = glShape			# the shape mode passed to OpenGL when drawing points.
		self.glPolygonMode = glPolygonMode	# the polygon mode controls if the shape is displayed as polygons, lines or verticies.

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

class Line(Shape):
	def __init__(self, start, end, color):
		super(Line, self).__init__(
			[start, end],
			color,
			glShape = GL_LINES
		)

class Point(Shape):
	def __init__(self, p, color, pointSize=4):
		super(Point, self).__init__([p], color, glShape = GL_POINTS)
		self.pointSize = pointSize

	def draw(self):
		glPointSize(self.pointSize)
		super(Point, self).draw()
