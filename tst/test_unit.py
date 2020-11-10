
"""TESTS FOR QGOL

Be sure to name all tests test_***(something)***

examples of correct names:
test_square
test_
test_89

"""
from qgol import *
from obj.base import *
from obj import *
from img.colors import printbold
from tst.wrappers import *
import numpy as np



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

@qgtest(13)
def test_2cells():
	printbold("13: Testing usual errored case with 2 cells (randomized)")

	qg = find_error()(2)
	print(qg)
	qg.next()
	print(qg)
	assert qg.numconf() == 1
	return qg

@qgtest(14)
def test_3cells():
	printbold("14: Testing usual errored case with 3 cells (randomized)")

	qg = find_error()(3)
	print(qg)
	qg.next()
	print(qg)
	assert qg.numconf() > 0
	return qg

@qgtest(15)
def test_4cells():
	printbold("15: Testing usual errored case with 4 cells (randomized)")

	qg = find_error()(4)
	print(qg)
	qg.next()
	print(qg)
	assert qg.numconf() > 0
	return qg

@qgtest(16)
def test_crossing():
	printbold("16: Testing crossing (it should change the phase)")
	
	qg = QGOL()
	qg.bc[0,0,0] = Cell(True)
	qg.bc[0,1,1] = Cell(True)
	print(qg)
	qg.next()
	print(qg)
	assert qg.numconf() > 0
	return qg

def find_error():
	""" returns a function that finds errors in the unitary evolution of a cube """
	from random import randint
	try:
		from scipy.special import binom
	except ModuleNotFoundError:
		def fact(n):
			if n == 0: return 1
			else: return n * fact(n-1)
		def minifact(n,k):
			if n <= k: return 1
			else: return n * minifact(n-1)
		def binom(n,k):
			return minifact(n,k) // fact(n-k)

	def newpos(pos,mini=0):

		while True:
			x = randint(mini,mini+1)
			y = randint(mini,mini+1)
			z = randint(mini,mini+1)
			if (x,y,z) not in pos:
				break
		return x,y,z

	def errored(qg):
		return qg.numconf() < 1

	def error_finder(M=4):
		if M > 4: warn("M too big in error finder")
		k = 0
		while True:
			qg = QGOL()
			pos = []
			for _ in range(M):
				p = newpos(pos,0)
				qg.bc[p] = Cell(True)
				pos.append(p)
			qg.next()
			k += 1
			if errored(qg) or k > 2*binom(8,M):
				break
		return qg

	return error_finder

