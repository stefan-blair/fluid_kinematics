from pyglet.gl import *

from vectors import Vector
from graphics import Shape, Line, Point, raycast3D


defaultOptions = {
	# point A of bounding box.  Minimum values in each direction.
	'anchor' : Vector(-25, -25, -25),
	# point B of bounding box.  Maximum values in each direaction.
	'bounds' : Vector( 25,  25,  25),
	# the step in each direction.
	'fieldResolution' : Vector(5, 5, 5),
	# the color of the vector field lines.
	'fieldColor' : Vector(255, 0, 255),
	# determains if the vector field lines should be drawn.
	'fieldVisible' : True,
	# the color of the particles.
	'particleColor' : Vector(255, 255, 0),
	# determains if the particles should be drawn.
	'particleVisible' : True,
	# determains if pathlines of each particle should be drawn.
	'pathlines' : False,
	# the size of each timestep forwards when calculating the next point in time.
	'pathResolution' : 0.5,
	# the color of the pathlines.
	'pathColor' : Vector(0, 255, 255),
}

class VisualField(Shape):
	def __init__(self, field, shapes, options={}, particles=[] ):
		super(VisualField, self).__init__([])

		self.field = field
		self.shapes = shapes
		self.particles = particles

		for option in defaultOptions:
			if option not in options:
				options[option] = defaultOptions[option]

		self.anchor = options['anchor']
		self.bounds = options['bounds']
		self.fieldResolution = options['fieldResolution']
		self.fieldColor = options['fieldColor']
		self.fieldVisible = options['fieldVisible']
		self.particleColor = options['particleColor']
		self.particleVisible = options['particleVisible']
		self.pathlines = options['pathlines']
		self.pathResolution = options['pathResolution']
		self.pathColor = options['pathColor']

		if self.pathlines:
			self.renderPathlines()

		self.raycast()

		self.retime(0)

	def raycast(self):
		print('raycasting...')
		x1, y1, z1 = self.anchor.asArray()
		x2, y2, z2 = self.bounds.asArray()
		xg, yg, zg = self.fieldResolution.asArray()

		shapes = self.shapes

		xl = []
		for x in xrange( x1, x2, xg ):
			yl = []
			for y in xrange( y1, y2, yg ):
				zl = []
				for z in xrange( z1, z2, zg ):
					point = Vector(x, y, z)
					zl.append(raycast3D(shapes, point))
				yl.append(zl)
			xl.append(yl)
		self.raycasted = xl
		print('finished raycasting.')

	def render(self, frame):
		x1, y1, z1 = self.anchor.asArray()
		x2, y2, z2 = self.bounds.asArray()
		xg, yg, zg = self.fieldResolution.asArray()

		field = self.field
		elements = []
		raycasted = self.raycasted

		if self.fieldVisible:
			fieldColor = self.fieldColor
			for xi, x in enumerate(xrange(x1, x2, xg)):
				for yi, y in enumerate(xrange(y1, y2, yg)):
					for zi, z in enumerate(xrange(z1, z2, zg)):
						point = Vector(x, y, z)
						if not raycasted[xi][yi][zi]:
							continue
						v = field(point, frame)
						elements.append(Line(point, point + v, fieldColor))
		if self.particleVisible:
			particleColor = self.particleColor
			time = self.time
			for particle in self.particles:
				elements.append(Point(particle(time), particleColor, pointSize=6))

		if self.pathlines:
			for pathline in self.pathlines:
				elements.append(pathline)

		return elements

	def renderPathlines(self):
		shapes = self.shapes
		pathResolution = self.pathResolution
		pathColor = self.pathColor
		particles = self.particles
		elements = []

		for particle in particles:
			time = 0
			prev = particle(0)
			while True:
				time += pathResolution
				nextParticle = particle(time)
				if not raycast3D(shapes, nextParticle):
					break
				elements.append(Line(prev, nextParticle, pathColor))
				prev = nextParticle
		self.pathlines = elements


	def retime(self, time):
		self.time = time
		self.elements = self.render(time)

	def draw(self):
		for element in self.elements:
			element.draw()
