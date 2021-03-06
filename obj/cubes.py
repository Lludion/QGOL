""" Defines the Cubes class.
This class handles several cubes."""
from obj import Cube, QGOL_U
from collections import defaultdict
from log.log import logd,debg

def unitarycube():
	c = Cube()
	c.op = QGOL_U()
	return c

class Cubes:
	def __init__(self):
		""" This class handles several cubes thanks to 
		its .li field """
		self.li = defaultdict(unitarycube)

	def add(self,poscel,par):
		"""
		Adds a cube to the defaultdict li if it was
		not already there. It activates the right cell.
		"""
		x,y,z = poscel
		xc,yc,zc = self.pos(poscel,par)
		self.li[xc,yc,zc][x-xc,y-yc,z-zc].activate()
		debg((x-xc,y-yc,z-zc,xc,yc,zc))
		debg(self.li[xc,yc,zc])

	def pos(self,poscel,par,parityset=True):
		if not parityset:
			par = not (par % 2)
		ipar = 1 - int(par)
		x = poscel[0] - 1 * abs(poscel[0] % 2 - ipar)
		y = poscel[1] - 1 * abs(poscel[1] % 2 - ipar)
		z = poscel[2] - 1 * abs(poscel[2] % 2 - ipar)
		debg(x,y,z)
		return x,y,z

	def __repr__(self):
		return "Cubes:" + str(self.li)

