
class Position:
	""" A container for position.
	i,j,k should be integers. """	

	def __init__(self,i=0,j=0,k=0):
		self.x = int(i)
		self.y = int(j)
		self.z = int(k)
	
	def xyz(self):
		""" Returns a tuple of the three coordinates """
		return self.x,self.y,self.z

	def check(self):
		assert isinstance(self.x,int)
		assert isinstance(self.y,int)
		assert isinstance(self.z,int)
	
	def adjacent(a,b):
		return (a.x == b.x and a.y == b.y) or (a.z == b.z and a.y == b.y) or (a.x == b.x and a.z == b.z)
	
	def __repr__(self):
		return str((self.x,self.y,self.z))

