class QCube:
	""" A container for a Cube and an amplitude (alpha) """
	
	def __init__(self,cube=None,alpha=1):
		self.cube = cube
		self.alpha = alpha
	
	def __repr__(self):
		return "\\" + str(self.alpha) + ":" + str(self.cube) + "/"
