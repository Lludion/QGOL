from obj.config import *
import numpy as np
from collections import defaultdict
from efficient import probatab

class Super:

	def __init__(self):
		self.cs = defaultdict(Config)
		# No need to add the phase in the configs
		# It is handled in the dict value (as the amplitude)
		self.norm = 0

	def normc(self):
		norm = 0.
		# TODO : test use probatab for efficiency later
		for cc in self.cs:
			norm += np.mod(cc.alpha)
		self.norm = norm
		return norm

