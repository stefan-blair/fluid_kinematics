from vectors import Vector
from fields import VectorField, Pathline, materialDerivative
from graphics import Window, VisualField, Cube

window = Window( 600, 600, 'Fluid Kinematics' )

# bounding points for the box
cubeStart = Vector(-15, -15, 0)
cubeEnd = Vector(15, 15, 100)
# cube shape to be rendered as bounding box
# there will be two, one showing the particles and one showing the fields, seperately
particleCube = Cube(cubeStart, cubeEnd, Vector(255, 255))
fieldCube = Cube(cubeStart - Vector(0, 0, 100), cubeEnd - Vector(0, 0, 100), Vector(255, 255))

# add the cube shapes to the window for rendering
window.addShape(particleCube)
window.addShape(fieldCube)

# math and physics stuff here.  define a velocity field and its three dimensional functions
V = VectorField(
	u = lambda v, t: v.y / 2,
	v = lambda v, t: -v.x / 2,
 	w = lambda v, t: v.z / 2
)
# calculate the acceleration field by taking the material derivative of the velocity field
# this works also for any other attribute, such as temperature or pressure
A = materialDerivative(V)

# trace the paths of a bunch of particles in the field
pathlines = []
for x in range(-9,9,3):
	for y in range(-9, 9, 3):
		pathlines.append(Pathline(V, Vector(x, y, 2)))

# options for customizing the fields
options = {
	# contains field to within these bounds
	'anchor' : particleCube.start,
	'bounds' : particleCube.end,

	'fieldResolution' : Vector(7, 7, 7),
	'pathlines' : True,
	# hide the vector field
	'fieldVisible' : False,
	'pathResolution' : 0.2,
	'fieldColor' : Vector(255)
}
 
# visualize the velocity field with the given options
# note, only the pathlines are visible, not the actual fields
VField = VisualField(V, [particleCube], options, pathlines)
window.addShape(VField)

# here, render both the velocity and acceleration fields, with no particles
options['anchor'] = fieldCube.start
options['bounds'] = fieldCube.end
options['fieldVisible'] = True

VField = VisualField(V, [fieldCube], options)
options['fieldColor'] = Vector(0, 255)
AField = VisualField(A, [fieldCube], options)

window.addShape(VField)
window.addShape(AField)

# render the window
window.render()
