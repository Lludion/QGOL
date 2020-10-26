###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *

def test_cube():
	## Cube tests
	print("Cube created : ")
	c = Cube(Cell)
	print(c)
	print("Active cells initially :")
	print(len(c))
	print("Activation of a Cell:")
	c.activation(0,0,1)
	print(c)
	print("Making one step on the cube:")
	c.op = QGOL_U()
	print(c.f())
	print(c)


	## subscript tests

	print("Activating cell 0,0,0")
	c[0,0,0] = Cell(True)
	print(c)
	assert c[1,1,0].__bool__() and c[0,0,0].__bool__() and not c[0,0,1].__bool__() 

