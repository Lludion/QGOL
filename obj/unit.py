""" Defines a useful Unitary """
from obj.base import Unitary,Position
from obj.qcubes import QCubes
from obj.cube import Cube

class QGOL_U(Unitary):
	
	def __init_(self):
		""" Unitary of the Quantum Game of Life, by Arrighi & Grattage"""
		super().__init__()
	
	def apply(self,cube):
		""" Returns the obtained cubes, included in a QCubes object """
		qbs = QCubes()
		if len(cube) == 1:
			qbs.addc(cube.reversed(),1)
		elif len(cube) == 2:
			qbs.addc(cube.reversed(),int(bool(cube.cross()))*(1+1j)*self.sq2)
		else:
			# if no special configuration is met, 
			#it's as if they were alone
			qbs.addc(cube.reversed(),1)
		"""
		elif len(cube) == 3:
			return qbs ## TODO
			pos = cube.positions()
			a,b,c = pos
			if a.x != b.x and a.x != c.x:#a seul sur sa ligne
				if a.y != b.y and a.y != c.y:
					# bc commutation - tilted case
					qbs.addc(Cube().from_pos([Position(a.x,a.y,1-a.z),b,c]),-self.sq2)
					qbs.addc(Cube().from_pos([Position(b.x,a.y,1-a.z),b,c]),self.sq2)
				elif a.y != b.y and a.y == c.y:		
					self.difx_uy(a,b,c,qbs)			
				elif a.y == b.y and a.y != c.y:		
					self.difx_uy(a,c,b,qbs)
				elif a.y == b.y and a.y == c.y:# (else)
					# bc commutation - plane case
					qbs.addc(Cube().from_pos([Position(a.x,a.y,1-a.z),b,c]),self.sq2)
					qbs.addc(Cube().from_pos([Position(a.x,b.y,1-a.z),b,c]),self.sq2)
			else:
				pass
				#I am not sure to understand the rules....
		"""
		return qbs

	def difx_uy(self,a,b,c,qbs):
		""" Adds the right QCubes to qbs if 
		a.x != b.x anb b.x == c.x
		a.y != b.y and b.y != c.y
		(They have a different x from the first Position
		and b and y have different y)
		"""
		if c.z == a.z:
			if b.z == a.z:
				# The three cells are in the same plane
				# no - must be added.
				qbs.addc(Cube().from_pos([Position(a.x,b.y,a.z),b,c]),self.sq2)
				qbs.addc(Cube().from_pos([Position(a.x,b.y,1-a.z),b,c]),self.sq2)
			else:
				qbs.addc(Cube().from_pos([a,Position(a.x,b.y,b.z),c]),-self.sq2)
				qbs.addc(Cube().from_pos([a,Position(a.x,b.y,a.z),c]),self.sq2)
		else:
			if b.z == a.z:
				# No cells share a side
				qbs.addc(Cube().from_pos([a,b,c]),1)
			else:
				qbs.addp([Position(a.x,b.y,a.z),b,c],-self.sq2)
				qbs.addp([Position(a.x,b.y,b.z),b,c],self.sq2)

