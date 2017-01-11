# fluid_kinematics

## synopsis
this project provides a tool for interacting with, visualizing and calculating vector fields relating to fluid kinematics.
given fields such as velocity, use the material derivative to derive the acceleration field, or even further.
visualize these vector fields using a variety of display options.
additionally, plot the path of particles with given start positions through the fields, using pathlines.
find the missing component of incomplete vector fields using the continuity equation.

## example
an example.  first, calculated the acceleration field from the velocity field.  then, displayed both fields in different colors in a bounding box
```python
from vectors import Vector
# these imports are used for calculating fields and pathlines
from fields import VectorField, Pathline, materialDerivative
# these imports are used for visualizing fields
from graphics import Window, VisualField, Cube

window = Window( 600, 600, 'Fluid Kinematics' )

# bounding points for the box
cubeStart = Vector(-15, -15, 0)
cubeEnd = Vector(15, 15, 100)

# cube shape to be rendered as bounding box
fieldCube = Cube(cubeStart - Vector(0, 0, 100), cubeEnd - Vector(0, 0, 100), Vector(255, 255))

# add the cube shapes to the window for rendering
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

# options for customizing the fields
options = {
	# contains field to within these bounds
	'anchor' : fieldCube.start,
	'bounds' : fieldCube.end,
	# spacing of the lines of the vector field
	'fieldResolution' : Vector(7, 7, 7),
	# color of the lines of the vector field (red here)
	'fieldColor' : Vector(255)
}
 
# here, render both the velocity and acceleration fields
VField = VisualField(V, [fieldCube], options)

# make sure the acceleration is a different color (green)
options['fieldColor'] = Vector(0, 255)
AField = VisualField(A, [fieldCube], options)

window.addShape(VField)
window.addShape(AField)

# render the window
window.render()
```

## requirements
all required dependencies can be found in requirements.txt
