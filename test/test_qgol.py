
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *

## qGOL tests
import numpy as np

qg = QGOL()
qg.bc[0,0,0] = Cell(True)
qg.bc[3,3,0] = Cell(True)

print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
qg.next()
print(qg)
print(qg.s.normc())
