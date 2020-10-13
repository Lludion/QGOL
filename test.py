###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *

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

c[0,0,0] = Cell(True)
print(c)

## qGOL tests
import numpy as np

qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[3,3,0] = Cell(True)

print(qg.s.cs)
print(qg.next())
print(qg.s.cs)
print(qg.next())
print(qg.s.cs)
print(qg.next())
print(qg.s.cs)
print(qg.s.normc())
