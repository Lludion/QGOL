
class Position:
	""" A container for position.
	i,j,k should be integers. """	

	def __init__(self,i,j,k):
		self.x = i
		self.y = j
		self.z = k
	
	def xyz(self):
		""" Returns a tuple of the three coordinates """
		return self.x,self.y,self.z

	def check(self):
		assert isinstance(self.x,int)
		assert isinstance(self.y,int)
		assert isinstance(self.z,int)
	
	def __repr__(self):
		return str((self.x,self.y,self.z))
