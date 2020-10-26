
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *
from sys import argv

## qGOL tests
import numpy as np
z = []
for arg in argv:
	try:
		z.append(int(arg))
	except ValueError:
		pass

def getz(n):
	return n in z or not z


def test_stablesquare():
	if getz(1):
		print("1: Testing stability of the well placed square")
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


def test_unstablesquare():
	if getz(2):
		print("2: Testing unstability of the ill placed square")
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


def test_walls():
	if getz(3):
		print("3: Testing Walls")
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

def test_wallbounce():
	if getz(4):
		print("4: Testing Wall bounce")
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

def test_LZaxis():
	if getz(5):
		print("5: Testing Rule 3: L shape along Z axis")
		qg = QGOL()
		qg.bc[0,0,0] = Cell(True)
		qg.bc[0,0,1] = Cell(True)
		qg.bc[1,0,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)

def test_dislocLZaxis():
	if getz(6):
		print("6: Testing Rule 3: Dislocated L shape along Z axis")
		qg = QGOL()
		qg.bc[0,0,0] = Cell(True)
		qg.bc[0,0,1] = Cell(True)
		qg.bc[1,1,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)

def test_LXaxis():
	if getz(7):
		print("7: Testing Rule 3: L shape along X axis")
		qg = QGOL()
		qg.bc[1,1,1] = Cell(True)
		qg.bc[1,1,0] = Cell(True)
		qg.bc[0,1,0] = Cell(True)



		print(qg)
		qg.next()
		print(qg)

def test_dislocLXaxis():
	if getz(8):
		print("8: Testing Rule 3: dislocated L shape along X axis")
		qg = QGOL()
		qg.bc[1,0,1] = Cell(True)
		qg.bc[1,1,0] = Cell(True)
		qg.bc[0,1,0] = Cell(True)



		print(qg)
		qg.next()
		print(qg)


def test_dislocLYaxis():
	if getz(9):
		print("9: Testing Rule 3 and further evolution: dislocated L shape along Y axis")
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

def test_L_usual():
	if getz(10):
		print("10: Testing Rule 3 and further evolution: usual L shape")
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

def test_L_usual2():
	if getz(11):
		print("11: Testing Rule 3 and further evolution: another usual L shape")
		qg = QGOL()
		qg.bc[-1,0,0] = Cell(True)
		qg.bc[-1,1,0] = Cell(True)
		qg.bc[-1,0,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)

def test_hadamard():
	if getz(12):
		print("12: Implementing a Hadamard Gate")

		qg = QGOL()
		qg.bc[0,0,0] = Cell(True)
		qg.bc[0,1,0] = Cell(True)
		qg.bc[-1,1,0] = Cell(True)
		qg.bc[-1,0,0] = Cell(True)
		qg.bc[1,1,0] = Cell(True)
		qg.bc[1,0,0] = Cell(True)
		qg.bc[2,1,0] = Cell(True)
		qg.bc[2,0,0] = Cell(True)
		qg.bc[1,-2,3] = Cell(True)
		qg.bc[5,-6,7] = Cell(True)
		qg.bc[-20,-18,19] = Cell(True)

		print(qg)
		qg.next()
		print(qg)
		qg.next()
		print(qg)
		qg.next()
		print(qg)
		for _ in range(100):
			qg.next()
		print(qg)



