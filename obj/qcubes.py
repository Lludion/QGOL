from obj.base import QCube
from obj.cube import Cube

class QCubes:
	
	def __init__(self,cubes=[]):
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
