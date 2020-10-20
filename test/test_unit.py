
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *
"""
## qGOL tests
import numpy as np

print("Testing stability of the well placed square")
qg = QGOL()
qg.bc[6,6,40] = Cell(True)
qg.bc[6,7,40] = Cell(True)
qg.bc[5,7,40] = Cell(True)
qg.bc[5,6,40] = Cell(True)


print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)

print("Testing unstability of the ill placed square")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[0,1,0] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[1,0,0] = Cell(True)


print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)


print("Testing Walls")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[0,1,0] = Cell(True)
qg.bc[-1,1,0] = Cell(True)
qg.bc[-1,0,0] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[1,0,0] = Cell(True)
qg.bc[2,1,0] = Cell(True)
qg.bc[2,0,0] = Cell(True)

print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)

print("Testing Wall bounce")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[0,1,0] = Cell(True)
qg.bc[-1,1,0] = Cell(True)
qg.bc[-1,0,0] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[1,0,0] = Cell(True)
qg.bc[2,1,0] = Cell(True)
qg.bc[2,0,0] = Cell(True)
qg.bc[3,3,3] = Cell(True)
print("Wandering cell in position : ",[(x,y,z) for conf in qg.s.cs for (x,y,z) in conf.tuple() if z])


print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
print("Wandering cell in position : ",[(x,y,z) for conf in qg.s.cs for (x,y,z) in conf.tuple() if z])


"""


"""
print("Testing Rule 3: L shape along Z axis")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[0,0,1] = Cell(True)
qg.bc[1,0,1] = Cell(True)



print(qg)
qg.next()
print(qg)

print("Testing Rule 3: Dislocated L shape along Z axis")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[0,0,1] = Cell(True)
qg.bc[1,1,1] = Cell(True)



print(qg)
qg.next()
print(qg)
"""

print("Testing Rule 3: L shape along X axis")
qg = QGOL()
qg.bc[1,1,1] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[0,1,0] = Cell(True)



print(qg)
qg.next()
print(qg)

print("Testing Rule 3: dislocated L shape along X axis")
qg = QGOL()
qg.bc[1,0,1] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[0,1,0] = Cell(True)



print(qg)
qg.next()
print(qg)

print("Testing Rule 3 and further evolution: dislocated L shape along Y axis")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[1,1,1] = Cell(True)
qg.bc[0,1,0] = Cell(True)



print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)

print("Testing Rule 3 and further evolution: usual L shape")
qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[1,1,0] = Cell(True)
qg.bc[1,0,0] = Cell(True)



print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)

