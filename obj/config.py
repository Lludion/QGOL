from obj.base import Cell
from collections import defaultdict

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

