 """ The Quantum Game of Life """
from obj import Super, Econfig
from log.log import logd,warn,debg

class QGOL:

	@logd
	def __init__(self,conf0=None):
		self.s = Super()
		self.step = 0
		if conf0 is None:
			# using the default configuration
			baseconf = Econfig()
			baseconf[0,0,0] = True
			self.s.cs[baseconf] = 1
			self.bc = baseconf # use for test purposes

	@logd
	def next(self):
		""" Executes a step H """
		debg("STEP : ",self.step,"PARITY:",self.pstep())
		debg("IPAR : ",1 - self.pstep())
		newsuper = Super()
		for conf,alpha in self.s.cs.items():
			if alpha:
				li = conf.evolution(self.pstep(),alpha)
				# extremely sub optimal, a list should never be used for a superposition
				# use a superposition (Super object) instead
				for a,conf in li:
					newsuper[conf] += a
		self.s = newsuper
		self.step += 1

	@logd
	def pstep(self):
		""" Returns the parity of the step. 
		 begins with an even step """
		return not (self.step % 2)

	def __repr__(self):
		return "QGOL on step " + str(self.step) + " : " + str(self.s.cs)

