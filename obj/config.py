""" Defines the Config class """
from obj.base import Cell
from collections import defaultdict
from log.log import logd,warn,debg

class Config:

	def __init__(self):
		""" A Configuration of Cells.
		This is not a Quantum object."""
		self.q = Cell()
		self._c = defaultdict(self.quiescent)

	def tuple(self):
		""" returns a tuple of the activated locations """
		return tuple([k for k,v in self._c.items() if v])

	def show_tuple(self,msk=[]):
		""" returns a tuple of the locations that are both activated and marked """
		return tuple([k for k,v in self._c.items() if v and k not in msk])

	def conf(self,i1,i2,i3):
		# unused
		return self._c[i1,i2,i3]
	
	def cell_number(self):
		""" Alias for len(self) """
		return len(self)

	def quiescent(self,*args,**kwargs):
		return self.q
	
	def __key(self):
		return self.tuple()

	def __hash__(self):
		return hash(self.__key())

	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__key() == other.__key()
		return NotImplemented

	def __getitem__(self, item):
		''' Returning the corresponding Cell '''
		return self._c[item]

	def __setitem__(self, key, item):
		""" Setting the corresponding Cell """
		if item.__class__ != Cell:
			item = Cell(item)
		item.p = key
		self._c[key] = item
	
	def __len__(self):
		return len(self.tuple())
	
	def __repr__(self):
		return str(self.show_tuple())
	
	def copy(self):
		""" shallow copy """
		nc = self.__class__()
		nc.q = self.q
		for k,v in self._c.items():
			nc[k] = v
		return nc

from obj.cubes import Cubes

class Econfig(Config):
	def __init__(self):
		""" A Configuration of Cells that may evolve
		This is not a Quantum object."""
		super().__init__()

	def evolution(self,par,alpha):
		licube = Cubes()
		for pos,cell in self._c.items():
			if cell.v:
				licube.add(pos,par)
			else:
				del self._c[pos]
		debg("Initial cubes ",licube)
		# here all the cubes have been created and cells have been activated
		qbsli = []
		for pos,ac in licube.li.items():
			qbsli.append((pos,ac.f()))
		debg("QBSLI (list of modified cubes (QCubes) and their position)",qbsli)
		cl = create_li(qbsli,0,[(alpha,Econfig())])
		debg("CREATED LI : ",str(cl))
		return cl

def create_li(qbsli,i,newsuper):
	""" all qcubes < i have been dealt with """
	# newsuper is a list of amplitude,conf
	if i >= len(qbsli):# all qcubes have been tensored into configs
		return newsuper
	litot = [] # full list
	qcubepos,qcubes = qbsli[i]# position of the current qcube
	for qcube in qcubes.cubes:
		nl = []
		alpha = qcube.alpha
		cube = qcube.cube
		x,y,z = qcubepos
		act = [cellpos.xyz() for cellpos in cube.positions()]
		debg("POSITIONS OF THE CELLS :",act)
		debg("POSITIONS OF THE QCUBE :",(x,y,z))
		act = [(a+x,b+y,c+z) for (a,b,c) in act]
		for a,conf in newsuper:
			nc = conf.copy()
			for pos in act:
				nc[pos].activate()
			nl.append((a*alpha,nc))
		litot += create_li(qbsli,i+1,nl)
	return litot		



