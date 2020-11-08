""" Defines a usable Unitary class """
from obj.base import Unitary,Position
from obj.qcubes import QCubes
from obj.cube import Cube
from log.log import logd,warn,debg
from obj.partition import *

class QGOL_U(Unitary):
	
	def __init_(self):
		""" Unitary of the Quantum Game of Life, by Arrighi & Grattage"""
		super().__init__()

	@logd
	def apply(self,cube):
		""" Returns the obtained cubes, included in a QCubes object """
		qbs = QCubes()
		if len(cube) == 1:
			qbs.addc(cube.reversed(),1)
		elif len(cube) == 2:
			pos = cube.positions()
			a,b = pos
			if a.adjacent(b):
				qbs.addc(cube.copy(),1)
			else:
				if cube.cross():
					qbs.addc(cube.reversed(),(1+1j)*self.sq2)
				else:
					qbs.addc(cube.reversed(),1)

		elif len(cube) == 3:
		
			debg("**********3************")
			pos = cube.positions()
			debg("INIT:",pos)
			a,b,c = pos
			inl = partition_edge(pos)
			if not inl:
				qbs.addc(cube.reversed(),1)
			else:
			 
				inLresult = PosGroup([a,b,c]).inL()
				if inLresult:
					inp,gr,inputval = inLresult
					
					x0,x1,y0,y1,z0,z1 = faces = partition(pos)
					pos1,pos2 = gr.li
					axes = gr.c
					if 'z' not in axes:
						xv,yv = gr.v
						if inputval:
							face1 = [f for f in faces if f.c == 'x' and f.v == xv][0]
							face2 = [f for f in faces if f.c == 'y' and f.v == yv][0]
							if find_contam(a,b,c,face1,pos) == inp:
								newinp = Position(xv,inp.y,inp.z)
							else:
								newinp = Position(inp.x,yv,inp.z)
						else:
							newinp = inp
						
						newpos1 = Position(newinp.x,newinp.y,not newinp.z)
						newpos2 = Position(not xv, not yv, not newinp.z)
					if 'x' not in axes:
						yv,zv = gr.v
						if inputval:
							face1 = [f for f in faces if f.c == 'y' and f.v == yv][0]
							face2 = [f for f in faces if f.c == 'z' and f.v == zv][0]
							if find_contam(a,b,c,face1,pos) == inp:
								newinp = Position(inp.x,yv,inp.z)
							else:
								newinp = Position(inp.x,inp.y,zv)
						else:
							newinp = inp
						newpos1 = Position(not newinp.x,newinp.y,newinp.z)
						newpos2 = Position(not newinp.x, not yv, not zv)
					if 'y' not in axes:
						zv,xv = gr.v
						if inputval:
							face1 = [f for f in faces if f.c == 'z' and f.v == zv][0]
							face2 = [f for f in faces if f.c == 'x' and f.v == xv][0]
							if find_contam(a,b,c,face1,pos) == inp:
								newinp = Position(inp.x,inp.y,zv)
							else:
								newinp = Position(xv,inp.y,inp.z)
						else:
							newinp = inp
						newpos1 = Position(newinp.x,not newinp.y,newinp.z)
						newpos2 = Position(not xv, not newinp.y, not zv)
					
					cube1 = Cube()
					cube1.from_pos([pos1,pos2,newpos1])
					cube2 = Cube()
					cube2.from_pos([pos1,pos2,newpos2])
					debg("Cube1:",[pos1,pos2,newpos1])
					debg("Cube2:",[pos1,pos2,newpos2])
					qbs.addc(cube1,self.sq2)
					qbs.addc(cube2,((-1)**inputval)*self.sq2)
				else:
					#"Dispersed" case (no common face)
					debg("Dispersed case:",pos)
					qbs.addc(cube.reversed(),1)
					
			debg("***********************")
		elif len(cube) == 4:
			debg("cube of size 4, qbs was:",qbs)
			debg('adding : ',cube.walled())
			qbs.addc(cube.walled(),1) # reverse, identity if wall
			debg("cube of size 4, qbs is:",qbs)
		elif len(cube) == 5:
			qbs.addc(cube.walled(),1)
		else:
			# if no special configuration is met, 
			# it's as if they were alone. However, with 6
			# active cells or more, there is a wall, so 
			# nothing should move to avoid wall destruction !
			# (it could be possible to make everything move - anyway)
			qbs.addc(cube.copy(),1)
		debg("in .apply : Calculating from ",cube,"\nto:\n",qbs)
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

