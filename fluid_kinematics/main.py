from vectors import Vector
from fields import VectorField, Pathline, materialDerivative
from graphics import Window, Shape, Line, Point, ObjFile, raycast3D, VisualField


window = Window( 600, 600, 'main' )

window.addShape(Line(Vector(),Vector(1000),Vector(255,0,0)))
window.addShape(Line(Vector(),Vector(0,1000),Vector(0,255,0)))
window.addShape(Line(Vector(),Vector(0,0,1000),Vector(0,0,255)))


obj = ObjFile('container.obj')

for shape in obj.shapes:
	shape.points = map(lambda p:p*5 + Vector(10), shape.points)

map( lambda s: window.addShape(s), obj.shapes)


V = VectorField(
	u = lambda v, t: -v.x/5 + t*2,
	w = lambda v, t: v.z/5 + t*2,
)
A = materialDerivative(V)

p = Vector(10, 0, -5)
P = Pathline(V, p)

#pathlines = []
#for z in xrange(-5, 5):
#	pathlines.append(Pathline(V, Vector(10, 0, z) ) )

#field, shapes, anchor=Vector(-25,-25,-25), bounds=Vector(25,25,25), gran=Vector(5,5,5), timestep, renderDistance
g = 3
r = 15 * g
options = {
	'anchor' : Vector(0, 0, -r),
	'bounds' : Vector(r, 1, r),
	'fieldResolution' : Vector(g, 1, g),
	'pathlines' : True,
	'pathResolution' : 0.2
}
VField = VisualField(V, obj.shapes, options, [P])
#AField = VisualField(A, obj.shapes, anchor=Vector(0, 0, -r), bounds=Vector(r, 1, r), gran=Vector(g,1,g), fieldColor=Vector(z=255) )

window.addShape(VField)
#window.addShape(AField)

window.render()
