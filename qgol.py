""" The Quantum Game of Life """
from obj import Super, Config

class QGOL:
	
	def __init__(self,conf0=None):
		self.s = Super()
		self.step = 0
		if conf0 is None:
			# using the default configuration
			baseconf = Config()
			baseconf[0,0,0] = True
			self.s.cs[baseconf] = 1
	
	def pstep(self):
		""" Returns the parity of the step. 
		 begins with an even step """
		return not self.step % 2

	
					



