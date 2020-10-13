from obj.base import Position, Cell

class Cube:
	
	def __init__(self,op=None,celltype=Cell):
		""" A cube of eight cells.
		Cells are of the provided celltype """
		if celltype is None:
			self.cube = None
		else:
			self.cube = [[[celltype() for _ in range(2)] for _ in range(2)] for _ in range(2)]
		self.op = op
		self.p = None # position (unused)

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
		return [(i,j,k,ip,jp,kp) for i in range(2) for k in range(2) for j in range(2) for ip in range(2) for jp in range(2) for kp in range(2) if (i,j,k) != (ip,jp,kp) and not (ip,jp,kp) not in self.adj(i,j,k) and self[i,j,k].v and self[ip,jp,kp]]

	def f(self):
		""" Applies the Unitary associated with this Cube."""
		if self.op is None:
			raise Exception("No operator provided.\nPlease provide a valid Unitary object to Transform this Cube.")
		else:
			return self.op.apply(self)

	def positions(self):
		""" Returns the list of positions of the activated cells in the Cube """
		return [Position(i,j,k) for i in range(2) for k in range(2) for j in range(2) if self[i,j,k]]

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

