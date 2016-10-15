from pyglet.gl import *
from pyglet.window import key

from vectors import Vector
from shape import Line

class Window(pyglet.window.Window):
	xRotation = yRotation = 30
	scale = 2

	def __init__(self, width, height, title='', rotationIncrement = 5, scaleIncrement = 1, time = 0, timestep = 1):
		super(Window, self).__init__(width, height, title)
		self.rotationIncrement = rotationIncrement
		self.scaleIncrement = scaleIncrement

		self.timestep = timestep
		self.time = time

		self.shapes = [
			Line(Vector(), Vector(1000), Vector(255,0,0)),
			Line(Vector(), Vector(0, 1000), Vector(0, 255, 0)),
			Line(Vector(), Vector(0, 0, 1000), Vector(0, 0, 255))
		]
		
		glClearColor(0, 0, 0, 1)
		glEnable(GL_DEPTH_TEST)

	def addShape(self, shape):
		self.shapes.append(shape)

	def render(self):
		pyglet.app.run()

	def on_draw(self):
		# Clear the current GL Window
		self.clear()

		# Push Matrix onto stack
		glPushMatrix()

		glRotatef(self.xRotation, 1, 0, 0)
		glRotatef(self.yRotation, 0, 1, 0)

		glScalef(self.scale, self.scale, self.scale)

		# Draw the six sides of the cube

		for shape in self.shapes:
			shape.draw()

		# Pop Matrix off stack
		glPopMatrix()
		
	def on_resize(self, width, height):
		glViewport(0, 0, width, height)

		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		aspectRatio = width / height
		gluPerspective(35, aspectRatio, 1, 10000)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		glTranslatef(0, 0, -400)

	def on_text(self, motion):
		if motion == '=':
			self.scale += self.scaleIncrement
		elif motion == '-':
			self.scale -= self.scaleIncrement
		elif motion == 'd':
			self.yRotation -= self.rotationIncrement
		elif motion == 'a':
			self.yRotation += self.rotationIncrement
		elif motion == 's':
			self.xRotation -= self.rotationIncrement
		elif motion == 'w':
			self.xRotation += self.rotationIncrement

	def on_text_motion(self, motion):
		if motion == key.RIGHT:
			self.time += self.timestep
		elif motion == key.LEFT:
			self.time -= self.timestep
		else:
			return
	
		for shape in self.shapes:
			shape.retime(self.time)
			
