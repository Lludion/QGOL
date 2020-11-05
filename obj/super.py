""" Defines the Super class """
from obj.config import *
import numpy as np
from collections import defaultdict
from efficient import probatab

class Super:

    def __init__(self):
        self.cs = defaultdict(np.complex)
        # No need to add the phase in the configs
        # It is handled in the dict value (as the amplitude)
        self.norm = 0

    def normc(self):
        norm = 0.
        # TODO : test use probatab for efficiency later
        for _,alpha in self.cs.items():
            norm += np.abs(alpha)**2
        self.norm = norm
        return norm
        
    def __getitem__(self,key):
        return self.cs[key]
        
    def __setitem__(self,key,item):
        self.cs[key] = item
        
    def copy(self):
        sup = Super()
        sup.cs = self.cs.copy()
        return sup

