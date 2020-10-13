""" A file where Gate Classes are implemented. """

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
