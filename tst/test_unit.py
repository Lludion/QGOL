
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *
from sys import argv
from img.colors import printbold

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

def parametrized(dec):
    def layer(*args, **kwargs):
        def repl(f):
            return dec(f, *args, **kwargs)
        return repl
    return layer

@parametrized
def qgtest(f, n):
    def aux(*xs, **kws):
    	if getz(n):
		    qg = f(*xs, **kws)
		    qg.cellconservation()
		    return qg
    return aux

@qgtest(1)
def test_stablesquare():
	printbold("1: Testing stability of the well placed square")
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
	return qg

@qgtest(2)
def test_unstablesquare():
	if getz(2):
		printbold("2: Testing unstability of the ill placed square")
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
		return qg

@qgtest(3)
def test_walls():
	if getz(3):
		printbold("3: Testing Walls")
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
		return qg

@qgtest(4)
def test_wallbounce():
	if getz(4):
		printbold("4: Testing Wall bounce")
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
		
		return qg

@qgtest(5)
def test_LZaxis():
	if getz(5):
		printbold("5: Testing Rule 3: L shape along Z axis")
		qg = QGOL()
		qg.bc[0,0,0] = Cell(True)
		qg.bc[0,0,1] = Cell(True)
		qg.bc[1,0,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)
		return qg

@qgtest(6)
def test_dislocLZaxis():
	if getz(6):
		printbold("6: Testing Rule 3: Dislocated L shape along Z axis")
		qg = QGOL()
		qg.bc[0,0,0] = Cell(True)
		qg.bc[0,0,1] = Cell(True)
		qg.bc[1,1,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)
		return qg

@qgtest(7)
def test_LXaxis():
	if getz(7):
		printbold("7: Testing Rule 3: L shape along X axis")
		qg = QGOL()
		qg.bc[1,1,1] = Cell(True)
		qg.bc[1,1,0] = Cell(True)
		qg.bc[0,1,0] = Cell(True)



		print(qg)
		qg.next()
		print(qg)
		return qg

@qgtest(8)
def test_dislocLXaxis():
	if getz(8):
		printbold("8: Testing Rule 3: dislocated L shape along X axis")
		qg = QGOL()
		qg.bc[1,0,1] = Cell(True)
		qg.bc[1,1,0] = Cell(True)
		qg.bc[0,1,0] = Cell(True)



		print(qg)
		qg.next()
		print(qg)
		return qg

@qgtest(9)
def test_dislocLYaxis():
	if getz(9):
		printbold("9: Testing Rule 3 and further evolution: dislocated L shape along Y axis")
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
		return qg

@qgtest(10)
def test_L_usual():
	if getz(10):
		printbold("10: Testing Rule 3 and further evolution: usual L shape")
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
		return qg

@qgtest(11)
def test_L_usual2():
	if getz(11):
		printbold("11: Testing Rule 3 and further evolution: another usual L shape")
		qg = QGOL()
		qg.bc[-1,0,0] = Cell(True)
		qg.bc[-1,1,0] = Cell(True)
		qg.bc[-1,0,1] = Cell(True)



		print(qg)
		qg.next()
		print(qg)
		return qg

@qgtest(12)
def test_hadamard():
	printbold("12: Implementing a Hadamard Gate")

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
	qg.evolve(100)
	print(qg)
	assert qg.numconf() == 8
	return qg

