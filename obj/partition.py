
class PosGroup:
	
	def __init__(self,li=None,c='x',v=0):
		if li is None:
			li = []
		self.li = li
		self.c = c # coord : 'x', 'y' or 'z'
		self.v = v # value : 0 or 1

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

