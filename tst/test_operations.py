""" Tests for operations on configurations """

from ope.operations import *
from img.colors import printbold
from obj.base import Pos
from qgol import *

def test_cube():
	printbold("1: Cube creation")
	qg = QGOL()
	msk = fullcube(qg.bc,Pos(0,0,0),2)
	qg2 = list(qg.s.cs.keys())[0].tuple()
	print(qg)
	qg.next()
	print(qg)
	k = qg.s.cs.keys()
	print(k)
	k = list(k)[0].tuple()
	print(k)
	print([x for x in qg2 if x not in k])
	for i in range(2,10):
		qg = QGOL()
		msk = fullcube(qg.bc,Pos(0,0,0),2*i)
		qg2 = list(qg.s.cs.keys())[0].tuple()
		qg.next()
		k = qg.s.cs.keys()
		k = list(k)[0].tuple()
		print(2*i,[x for x in qg2 if x not in k])

test_cube()

def test_tunnel():
	printbold("2: Testing stability of the tunnel")
	qg = QGOL()
	qg.bc[2,0,0].activate()
	msk = tunnelx(qg.bc,Pos(0,-1,-1),6)
	qg.s.mask += msk
	print(qg)
	qg.next()
	print(qg)
	qg.next()
	print(qg)
	qg.next()
	print(qg)

test_tunnel()
