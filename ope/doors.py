"""
Doors class.

It is assumed that each door is built so that the qubit only ever goes to the right (x only increases) 
"""

def enable(s,pos):
	for p in pos:
		s[p].activate()

class Door:
	
	def __init__(self,sd=1):
		self.sd = 1  # step duration
		self.id = '\00'

	def generate(self,s,c,inep,outep=None):
		"""
		s is the step,
		c is the config,
		inep is the list of the input entry points
		outep is the list of the output entry points (unused now)
		"""
		raise NotImplemented("Abstract Class")
	
	def __str__(self):
		return "Door"+str(self.__class__.__name__)

class Rpi4(Door):
	def __init__(self,sd = 2):
		self.sd = sd # step duration
		self.id = '4'
	
	def generate(self,s,c,inep,outep=None):
		if outep is None:
			outep = []
		for qin in inep:
			x,y,z = qin
			xa,ya,za = x+1+s,y+1+s,z-s
			enable(c,[(xa,ya,za)])
			outep.append((x+self.sd,y+self.sd,z+self.sd))
		return s+self.sd, outep

class Crpi4(Door):
	def __init__(self,sd = 2):
		self.sd = sd # step duration
		self.id = 'c'
	
	def generate(self,s,c,inep,outep=None):
		""" currently identical to Rpi4 """
		if outep is None:
			outep = []
		for qin in inep:
			x,y,z = qin
			xa,ya,za = x+1+s,y+1+s,z-s
			enable(c,[(xa,ya,za)])
			outep.append((x+self.sd,y+self.sd,z+self.sd))
		return s+self.sd, outep
		
class Hadamard(Door):

	def __init__(self,sd=1):
		self.sd = 1  # step duration
		self.id = 'h'

	def generate(self,s,c,inep,outep=None):
		qin = inep[0]
		#qout = outep[0]
		x,y,z = qin
		#c[x,y,z] = None
		return s+self.sd,[(x,y,z)]

