""" The Quantum Game of Life """
from obj import Super, Econfig
from log.log import logd,warn,debg
from img.colors import bcolors as col

class QGOL:

    @logd
    def __init__(self,conf0=None):
        self.s = Super()
        self.step = 0
        if conf0 is None:
            # using the default configuration
            baseconf = Econfig()
            self.s.cs[baseconf] = 1
            self.bc = baseconf # use for test purposes

    @logd
    def next(self):
        """ Executes a step H """
        debg("STEP : ",self.step,"PARITY:",self.pstep())
        newsuper = Super()
        newsuper.mask = self.s.mask
        for conf,alpha in self.s.cs.items():
            if alpha:
                li = conf.evolution(self.pstep(),alpha)
                debg(li)
                # extremely sub optimal, a list should never be used for a superposition
                # use a superposition (Super object) instead
                for a,conf in li:
                    newsuper[conf] += a
            else:
                warn("step ",self.step," ; Suppressed a conf:",conf)
                print("Suppressed a conf :",conf)
        self.s = newsuper
        debg("mask:",self.s.mask)
        self.step += 1
    
    def evolve(self,n=1):
        """ Evolves for n steps.
        It executes n times the method .step
        """
        for _ in range(n):
            self.next()

    def pstep(self):
        """ Returns the parity of the step. 
         begins with an even step """
        return not (self.step % 2)

    def cellconservation(self):
        """ Tests whether no configuration has a different number of cells """
        confnum = [len(k) for k,v in self.s.cs.items() if v]
        debg([(k,len(k)) for k,v in self.s.cs.items() if v])
        assert not [False for n in confnum if n != confnum[0]]

    def numconf(self):
        """ Returns the number of active configurations """
        return len([False for _,v in self.s.cs.items() if v])

    def print_norm(self):
        n = self.s.normc()
        #logg.debug("norm:"+str(n))
        if abs(n) < 0.9:
            color = col.FAIL
        elif abs(n - 1)>1/100000:
            color = col.WARNING
        else:
            color = ""
        print(color , n , col.ENDC)
        return color

    def __repr__(self):
        return "QGOL on step " + str(self.step) + " : " + str(self.s)
    
    def copy(self):
        qgol = QGOL()
        qgol.step = self.step
        qgol.s = self.s.copy()
        return qgol

