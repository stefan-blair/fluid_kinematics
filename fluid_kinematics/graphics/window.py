import pyglet
from pyglet.gl import *
from pyglet.window import key

from shape import Shape
from vectors import Vector

class Window(pyglet.window.Window):
	xRotation = yRotation = 30
	scale = 2

	def __init__(self, width, height, title='', increment = 5, time = 0, timestep = 1):
		super(Window, self).__init__(width, height, title)
		self.increment = increment

		self.timestep = timestep
		self.time = time

		self.shapes = []


		glClearColor(0, 0, 0, 1)
		glEnable(GL_DEPTH_TEST)

	def addShape(self, shape):
		self.shapes.append( shape )

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

	def on_key_press(self, symbol, modifiers):
		if symbol == 61:
			self.scale += 1
		elif symbol == 45:
			self.scale -= 1
		elif symbol == 97:
			self.yRotation -= self.increment
		elif symbol == 119:
			self.xRotation -= self.increment
		elif symbol == 115:
			self.xRotation += self.increment
		elif symbol == 100:
			self.yRotation += self.increment

	def on_text_motion(self, motion):
		if motion == key.RIGHT:
			self.time += self.timestep
		elif motion == key.LEFT:
			self.time -= self.timestep
		else:
			return
		print('current-time = ' + str(self.time))
		for shape in self.shapes:
			shape.retime(self.time)
