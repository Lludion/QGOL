""" Generation of quantum doors in a configuration (of Econfig type) 

It is assumed that each door is built so that the qubit only ever goes to the right (x only increases) 

"""

class Door:
	
	def __init__(self):
		pass

	def generate(self,c,inep,outep):
		"""
		c is the config,
		inep is the list of the input entry points
		outep is the list of the output entry points
		"""
		raise NotImplemented("LMAO")

class Hadamard(Door):

	def __init__(self):
		self.generate.__doc__ = super().generate.__doc__

	def generate(self,c,inep,outep):
		qin = inep[0]
		qout = outep[0]
		
		

z = Hadamard()
print(z.generate.__doc__)
print(Door().generate.__doc__)

