
###TESTS FOR QGOL
from qgol import *
from obj.base import *
from obj import *
from log.log import logg
from pytest import xfail
from img.colors import bcolors as col
from os import environ

def norm_verif(qg):
	color = qg.print_norm()
	if color == col.WARNING:
		xfail("Norm was a little bit off.")
	assert color != col.FAIL

def test_qgol(argv=None,repeat=30):
	print("Randomized tests")
	
	if not repeat:
		return

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
			if "r=" in arg:
				arg = arg[2:]
				try:
					repeat = int(arg)
				except ValueError:
					pass

	# Initialization
	print(f"Norm after {nsteps} steps:")

	norms = [0,0,0] # good, warning, bad
	for _ in range(repeat):
		qg = QGOL()
		zmax = (actcell//4) + 1
		for _ in range(actcell):
			i,j,k = randint(0,2),randint(0,2),randint(0,zmax)
			qg.bc[i,j,k] = Cell(True)
		#logg.debug(str(qg))
		#logg.debug(str(nsteps)+" steps, "+str(actcell)+' cells')

		qg.evolve(nsteps)
		n = qg.s.normc()
		if abs(n) < 0.9:
			norms[2] += 1
		elif abs(n - 1)>1/100000:
			norms[1] += 1
		else:
			norms[0] += 1

	print(f"{col.OKGREEN} Good : {norms[0]}/{repeat}\n{col.WARNING} Errored : {norms[1]}/{repeat}\n{col.FAIL} Failed : {norms[2]}/{repeat}{col.CEND}")
	if "PYTEST_CURRENT_TEST" in environ:# if launch from within pytest
		assert not norms[2]
		if norms[1]:
			xfail(f"Norm was a little bit off {norms[1]} times.")

