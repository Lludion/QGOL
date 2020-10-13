from obj.base import QCube
from obj.cube import Cube

class QCubes:
	
	def __init__(self,cubes=None):
		if cubes is None:
			cubes = []
		self.cubes = cubes

	def add(self,qcube):
		""" Adds a QCube """
		self.cubes.append(qcube)
	
	def addc(self,cube,alpha):
		""" Creates and Adds a QCube """
		self.cubes.append(QCube(cube,alpha))
	
	def addp(self,poslist,alpha):
		""" Creates and Adds a QCube from a position list or tuple"""
		self.cubes.append(QCube(Cube().from_pos(poslist),alpha))

	def __getitem__(self, item):
		''' returning the corresponding cell
		'''
		return self.cubes[item]

	def __setitem__(self, key, item):
		""" Setting the corresponding Cell """
		self.cubes[key] = item

	def __len__(self):
		""" returns the number of QCube s in .cubes """
		return len(self.cubes)
	
	def __repr__(self):
		return str(self.cubes)
