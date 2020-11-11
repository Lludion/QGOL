""" Tests for doors' creation """

from ope.generator import *
from img.colors import printbold
from obj.base import Pos
from qgol import QGOL
from tst.wrappers import *

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
	""" Testing Rpi4 door creation """
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
	return qg

