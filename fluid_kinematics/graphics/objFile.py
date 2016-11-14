from pyglet.gl import GL_POLYGON, GL_LINE

from vectors import Vector
from graphics import Shape

# this class describes a simple class which can
# read object (.obj) files, and holds a list of
# the objects file's attributes for later use.
# Each instance requires a file name, marking
# the name of the .obj file to read.

class ObjFile:
	def __init__(self, name):
		self.name = name
		f = file(name, 'r')
		data = f.read().split('\n')

		# an array of verticies (Vector objects) containing all vertex in the file
		self.verticies = []
		# an array of shapes (Vector array) containing all faces in the file
		self.shapes = []

		for d in data:
			components = d.split(' ')

			if components[0] == '#':
				# ignore comments, which start with '#'
				pass
			elif components[0] == 'v':
				# add verticies by casting components 1-3 into floats, and then vectors
				self.verticies.append(Vector(*map(float, components[1:4])))
			elif components[0] == 'f':
				# add faces by splitting each argument ( vertex / texture / normal ) into just ( vertex )
				# and casting to integers
				points = map(lambda s: self.verticies[ int(s.split('/')[0]) - 1 ], components[1:])
				shape = Shape(points, Vector( 0, 255, 255 ), glShape = GL_POLYGON, glPolygonMode = GL_LINE)
				self.shapes.append(shape)
		f.close()
