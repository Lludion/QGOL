from collections import defaultdict
import numpy as np
import numba

@numba.vectorize([numba.float64(numba.complex128),numba.float32(numba.complex64)])
def probatab(x):
	return x.real**2 + x.imag**2

class Gate:

	def __init__(self):
		self.x = 0 # dim x
		self.y = 0 # dim y
		self.fun = lambda x : [self.coord(x,j) for j in range(self.y)]

	def coord(self,i,j):
		if i == j:
			return 1
		else:
			return 0

	def __repr__(self,matrix=True):
		s = ""
		if matrix:
			for i in range(len(self.x)):
				s += "( "
				for j in range(len(self.y)):
					s += str(self.fun(i)[j]) + " "
				s += ")\n"
			else:
				for i in range(len(self.x)):
					s += str(i) + "-> "+ str(self.fun(i)) + "\n"
				
		return s
	
class Config:

	def __init__(self):
		""" A Configuration of Cells.
		This is not a Quantum object."""
		self.q = Cell()
		self.c = defaultdict(self.quiescent)

	def tuple(self):
		""" returns a tuple of the activated locations """
		return tuple([k for k,v in self.c.items() if v])

	def conf(i1,i2,i3):
		return self.c[i1,i2,i3]

	def quiescent(self,*args,**kwargs):
		return self.q
	
	def __key(self):
		return self.tuple()

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if isinstance(other, A):
			return self.__key() == other.__key()
		return NotImplemented

	def __getitem__(self, item):
		''' Returning the corresponding Cell '''
		return self.c[item]

	def __setitem__(self, key, item):
		""" Setting the corresponding Cell """
		if item.__class__ != Cell:
			item = Cell(item)
		self.c[key] = item
	
	def __repr__(self):
		return str(self.tuple())

class Super:

	def __init__(self):
		self.cs = defaultdict(Config)
		# No need to add the phase in the configs
		# It is handled in the key (as the amplitude)
		self.norm = 0

	def normc(self):
		norm = 0.
		for cc in self.cs:
			norm += np.mod(cc.alpha)
		self.norm = norm
		return norm

class Global:

	def __init__(self):
		self.name = ""
		self.evenstep = True

	def f(self):
		if self.evenstep:
			return

class Unitary(Gate):
	""" This is an object that will be used to
	transform what lies inside the Cubes."""
	
	def __init__(self):
		super().__init__()
		
	def apply(self,cube):
		""" Placeholder function """
		t = "Please implement the function you want to apply on the cubes."
		print(t)
		return t

class Cell:
	
	def __init__(self,v=False):
		""" A cell of the game of life.
		May have the value True or False.
		True means that the cell is activated
		False means that it is empty. 
		
		The value is accessed via the .v method"""
		self.v = v
	
	def activate(self):
		self.v = True
	
	def deactivate(self):
		self.v = False
	
	def negate(self):
		self.v = not self.v

	def __repr__(self):
		return str(int(self.v)) # + "@" + str(id(self))
	
	def __bool__(self):
		return self.v

class Cube:
	
	def __init__(self,op=None,celltype=Cell):
		""" A cube of eight cells.
		Cells are of the provided celltype """
		if celltype is None:
			self.cube = None
		else:
			self.cube = [[[celltype() for _ in range(2)] for _ in range(2)] for _ in range(2)]
		self.op = op

	def activation(self,*args):
		""" Activates the specified Cell. """
		if len(args) == 1:
			if type(args) == type(Cell()):
				for c in self.flatcube():
					if c == args[0]:
						c.activate()
		elif len(args) >= 3:			
			self.cube[args[0]][args[1]][args[2]].activate()
		elif len(args) == 2:
			raise NotImplementedError
		else:
			print("WARNING : You should use the .activate method instead.")
			self.activate()
		
	def reverse(self):
		""" Reverses the cube """
		nc = [[[Cell() for _ in range(2)] for _ in range(2)] for _ in range(2)]
		for i in range(len(self.cube)):
			for j in range(len(self.cube[i])):
				for k in range(len(self.cube[i][j])) :
					nc[1-i][1-j][1-k].v = self[i,j,k].v
		for i in range(len(self.cube)):
			for j in range(len(self.cube[i])):
				for k in range(len(self.cube[i][j])) :
					self.cube[i][j][k].v = nc[i][j][k].v
	
	def reversed(self):
		""" returns a reversed copy of the Cube """
		c  = self.copy()
		c.reverse(); return c
	
	def copy(self):
		""" Returns a shallow copy of the Cube """
		nc = Cube(self.op,None)
		nc.cube = [[[self[i,j,k] for k in range(2)] for j in range(2)] for i in range(2)]#shallow copy
		return nc
	
	def bump(self):
		""" Number of crossing particles """
		return len([False for i in range(2) for j in range(2) for k in range(2) if self[i,j,k].v and self[1-i,1-j,1-k].v])

	def adj(self,i,j,k):
		""" Adjacent cells of a given cell."""
		return [(ip,jp,kp) for ip in range(2) for jp in range(2) for kp in range(2) if (i==ip or k == kp or j == jp) and not (i,j,k)==(ip,jp,kp)]

	def cross(self):
		""" Crossing cells. We probably, like .bump, do NOT need the cells, only their number."""
		return [(i,j,k,ip,jp,kp) for i in range(2) for k in range(2) for j in range(2) for ip in range(2) for jp in range(2) for kp in range(2) if (i,j,k) != (ip,jp,kp) and not (ip,jp,kp) not in adj(i,j,k) and self[i,j,k].v and self[ip,jp,kp]]

	def f(self):
		""" Applies the Unitary associated with this Cube."""
		if self.op is None:
			raise Exception("No operator provided.\nPlease provide a valid Unitary object to Transform this Cube.")
		else:
			self.op.apply(self)
	
	def positions(self):
		""" Returns the list of positions of the activated cells in the Cube """
		return [Position(i,j,k) for i in range(2) for k in range(2) for j in range(2) if cube[i,j,k].v]
		
	def activate(self):
		""" activates all the Cells of a given Cube """
		for c in self.flatcube():
			c.activate()
				
	def flatcube(self):
		""" returns a list of all Cells in the Cube """
		return [c for l in self.cube for k in l for c in k]
	
	def cclass(self):
		"""returns the class of the first cell"""
		return self[0,0,0].__class__

	def from_pos(self,pos,newct=None):
		if newct is None:
			newct = self.cclass()
		self.cube = [[[newct() for _ in range(2)] for _ in range(2)] for _ in range(2)]
		for p in pos:
			if type(p) == type(Position()):
				self[p.x,p.y,p.z].v = True
			else:
				self[p[0],p[1],p[2]].v = True

	def __len__(self):
		""" returns the number of active cells """
		return len([False for l in self.cube for k in l for i in k if i.v])
	
	def len(self):
		""" returns the number of active cells """
		return len(self)

	def __getitem__(self, item):
		''' returning the corresponding cell
		print(item)
		print(self.cube)
		print(self.cube[item[0]])
		'''
		return self.cube[item[0]][item[1]][item[2]]

	def __setitem__(self, key, item):
		""" Setting the corresponding Cell """
		if item.__class__ != Cell:
			item = Cell(item)
		self.cube[key[0]][key[1]][key[2]]= item
	
	def __repr__(self):
		return "CUBE{" + str(id(self)) + "}:\n" + str(self.cube)

class Position:
	
	def __init__(self,i,j,k):
		self.x = i
		self.y = j
		self.z = k
	
	def xyz(self):
		return self.x,self.y,self.z

class QCube:
	
	def __init__(self,cube=None,alpha=1):
		self.cube = cube
		self.alpha = alpha

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
			qbs.addc(cube.reversed(),int(bool(cube.cross()))*(1+1j)/np.sqrt(2))
		elif len(cube) == 3:
			return qbs ## TODO
			pos = cube.positions()
			a,b,c = pos
			if a.x != b.x and a.x != c.x:#a seul sur sa ligne
				if a.y != b.y and a.y != c.y:
					# bc commutation - tilted case
					qbs.addc(Cube().from_pos([Position(a.x,a.y,1-a.z),b,c]),-1/np.sqrt(2))
					qbs.addc(Cube().from_pos([Position(b.x,a.y,1-a.z),b,c]),1/np.sqrt(2))
				elif a.y != b.y and a.y == c.y:		
					self.difx_uy(a,b,c,qbs)			
				elif a.y == b.y and a.y != c.y:		
					self.difx_uy(a,c,b,qbs)
				elif a.y == b.y and a.y == c.y:# (else)
					# bc commutation - plane case
					qbs.addc(Cube().from_pos([Position(a.x,a.y,1-a.z),b,c]),1/np.sqrt(2))
					qbs.addc(Cube().from_pos([Position(a.x,b.y,1-a.z),b,c]),1/np.sqrt(2))
			else:
				pass
				#I am not sure to understand the rules....
			
					
				
		else:
			pass
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
				qbs.addc(Cube().from_pos([Position(a.x,b.y,a.z),b,c]),1/np.sqrt(2))
				qbs.addc(Cube().from_pos([Position(a.x,b.y,1-a.z),b,c]),1/np.sqrt(2))
			else:
				qbs.addc(Cube().from_pos([a,Position(a.x,b.y,b.z),c]),-1/np.sqrt(2))
				qbs.addc(Cube().from_pos([a,Position(a.x,b.y,a.z),c]),1/np.sqrt(2))
		else:
			if b.z == a.z:
				# No cells share a side
				qbs.addc(Cube().from_pos([a,b,c]),1)
			else:
				qbs.addp([Position(a.x,b.y,a.z),b,c],-1/np.sqrt(2))
				qbs.addp([Position(a.x,b.y,b.z),b,c],1/np.sqrt(2))
							
class QGOL:
	
	def __init__(self,conf0=None):
		self.s = Super()
		self.step = 0
		if conf0 is None:
			# using the default configuration
			baseconf = Config()
			baseconf[0,0,0] = True
			self.s.cs[baseconf] = 1
	
	def pstep(self):
		""" Returns the parity of the step. 
		 begins with an even step """
		return not self.step % 2

	
					



