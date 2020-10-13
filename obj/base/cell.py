
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

