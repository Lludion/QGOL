
class PosGroup:
	
	def __init__(self,li=None,c='x',v=0):
		if li is None:
			li = []
		self.li = li
		self.c = c # coord : 'x', 'y' or 'z'
		self.v = v # value : 0 or 1

	def inL(self):
		""" checks whether the PosGroup is in a L shape or not. 
		If it is, it returns the "top" of the L (which is, the one
		Cell that should be 'moving' ) """
		try:
			a,b,c = self.li
		except ValueError:
			return False
		x0y0,x0y1,x1y0,x1y1,y0z0,y0z1,y1z0,y1z1,x0z0,x0z1,x1z0,x1z1 = parpos = partition_edge([a,b,c])
		inhab = [gr for gr in parpos if len(gr.li) >= 2]
		candi = []
		for gr in inhab:# inhabited groups
			for p in (a,b,c):
				if p not in gr:
					pass # TODO
		return False		

def partition(pos):
	""" returns a partition x0,x1,y0,y1,z0,z1 of the list ' pos '
	
	where, for instance:
	x0 = [p for p in pos if not p.x] """
	x0 = [p for p in pos if not p.x]
	x1 = [p for p in pos if p.x]
	y0 = [p for p in pos if not p.y]
	y1 = [p for p in pos if p.y]
	z0 = [p for p in pos if not p.z]
	z1 = [p for p in pos if p.z]
	return PosGroup(x0,'x',0),PosGroup(x1,'x',1),PosGroup(y0,'y',0),PosGroup(y1,'y',1),PosGroup(z0,'z',0),PosGroup(z1,'z',1)

def partition_edge(pos):
	""" partition around edges """
	x0y0 = [p for p in pos if not p.x and not p.y]
	x0y1 = [p for p in pos if not p.x and p.y]
	x1y0 = [p for p in pos if p.x and not p.y]
	x1y1 = [p for p in pos if p.x and p.y]
	y1z0 = [p for p in pos if p.y and not p.z]
	y1z1 = [p for p in pos if p.y and p.z]
	y0z0 = [p for p in pos if not p.y and not p.z]
	y0z1 = [p for p in pos if not p.y and p.z]
	x0z0 = [p for p in pos if not p.x and not p.z]
	x0z1 = [p for p in pos if not p.x and p.z]
	x1z0 = [p for p in pos if p.x and not p.z]
	x1z1 = [p for p in pos if p.x and p.z]
	return PosGroup(x0y0,'xy'),PosGroup(x0y1,'xy'),PosGroup(x1y0,'xy'),PosGroup(x1y1,'xy'),PosGroup(y0z0,'yz'),PosGroup(y0z1,'yz'),PosGroup(y1z0,'yz'),PosGroup(y1z1,'yz'),PosGroup(x0z0,'xz'),PosGroup(x0z1,'xz'),PosGroup(x1z0,'xz'),PosGroup(x1z1,'xz')

