""" Tests for doors' creation """

from ope.generator import *
from img.colors import printbold
from obj.base import Pos
from qgol import QGOL
from tst.wrappers import *
from img import generer_gif
from os import environ

@qgtest(1)
def test_crpi4():
	""" Testing Rpi4 door """
	qg = QGOL(  )
	qg.bc[0,0,0].activate()
	try:
		Rpi4().generate(2,qg.bc,[(2,2,2)],[])
		Rpi4().generate(6,qg.bc,[(6,6,6)],[])
	except BaseException as e:
		raise BaseException(e)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	return qg

@qgtest(2)
def test_crpi4():
	""" Testing Generation of a circuit using only phase(pi/4) doors.
	It models the Z gate."""
	qg = QGOL()
	qg.bc[0,0,0].activate()
	doorify(qg.bc,'4444')
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg.evolve()
	print(qg)
	qg = QGOL()
	qg.bc[0,0,0].activate()
	#adding two squares for scale
	qg.bc[-3,0,0].activate()
	qg.bc[-3,-1,0].activate()
	qg.bc[-4,-1,0].activate()
	qg.bc[-4,0,0].activate()
	qg.bc[0,-3,0].activate()
	qg.bc[0,-4,0].activate()
	qg.bc[-1,-4,0].activate()
	qg.bc[-1,-3,0].activate()
	
	doorify(qg.bc,'4444')
	generer_gif(qg,20,name='rpi4/')
	return qg

