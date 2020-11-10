""" Generation of quantum doors in a configuration (of Econfig type) 

It is assumed that each door is built so that the qubit only ever goes to the right (x only increases) 

"""

class Door:
	
	def __init__(self):
		pass

	def generate(self,s,c,inep,outep):
		"""
		s is the step,
		c is the config,
		inep is the list of the input entry points
		outep is the list of the output entry points
		"""
		raise NotImplemented("Abstract Class")

class Crpi4(Door):
	def __init__(self):
		pass
	
	def generate(self,s,c,inep,outep):
		x,y,z = qin = inep[0]
		
		w,t,a = cube = Cubes().pos(qin,s)
		if z == a + 1:
			#activate([(w,t,a),(w+1,t,a),(w,t+1,a),(w+1,t+1,a),(w,t,a+1),(w+1,t,a+1),(w,t+1,a+1),(w+1,t+1,a+1)])
			#create a good L
			#activate([w,t,a])
			pass
class Hadamard(Door):

	def __init__(self):
		pass

	def generate(self,s,c,inep,outep):
		qin = inep[0]
		qout = outep[0]
		x,y,z = qin
		c[x,y,z] = None
		

z = Hadamard()
print(z.generate.__doc__)
print(Door().generate.__doc__)

