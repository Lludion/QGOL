
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *
from log.log import logg
from pytest import xfail
from img.colors import bcolors as col

def norm_verif(qg):
	color = qg.print_norm()
	if color == col.WARNING:
		xfail("Norm was a little bit off.")
	assert color != col.FAIL

def test_qgol(argv=None):
	print("Randomized tests")

	## qGOL tests
	import numpy as np
	from random import randint
	if argv is None:
		from sys import argv

	#default values
	actcell = 6
	nsteps = 100


	actset = False
	for arg in argv:
		try:
			z = int(arg)
			if actset:
				nsteps = z
			else:
				actset = True
				actcell = z
		except ValueError:
			pass

	# Initialization

	qg = QGOL()
	zmax = (actcell//4) + 1
	for _ in range(actcell):
		i,j,k = randint(0,2),randint(0,2),randint(0,zmax)
		qg.bc[i,j,k] = Cell(True)
	#logg.debug(str(qg))
	#logg.debug(str(nsteps)+" steps, "+str(actcell)+' cells')

	qg.evolve(nsteps)

	print(f"Norm after {nsteps} steps:")
	norm_verif(qg)

