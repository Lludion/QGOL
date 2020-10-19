
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *

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


