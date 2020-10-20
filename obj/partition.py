from log.log import logd,logi

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
		Cell that should be 'moving' ),
		the PosGroup of the other two things
		the InputValue (0 or 1)"""
		try:
			a,b,c = pos = self.li
		except ValueError:
			return False
		x0y0,x0y1,x1y0,x1y1,y0z0,y0z1,y1z0,y1z1,x0z0,x0z1,x1z0,x1z1 = parpos = partition_edge([a,b,c])
		inhab = [gr for gr in parpos if len(gr.li) >= 2]
		candi = []
		if len(inhab) == 1:
			# Rotate until well placed, input is 1
			gr = inhab[0]
			for p in (a,b,c): # p is not with the others
				if p not in gr.li:
					return p,gr,1
		else:
			#3 are in a face
			x0,x1,y0,y1,z0,z1 = faces = partition(pos)
			fhab = [gr for gr in faces if len(gr.li) >= 3][0]
			#fhab = inhabited face
			for p in (a,b,c):
				if p not in fhab.li:
					raise BaseException("Unexpected case happened. Contact us.")
			contcell = find_contam(a,b,c,fhab,pos)
			stablegroup = [gr for gr in parpos if contcell not in gr.li and len(gr.li) == 2][0]
			return contcell,stablegroup,0
		return False

def find_contam(a,b,c,face,pos):
	""" returns a Position of the contaminated cell """
	void = [(0,0),(0,1),(1,0),(1,1)]
	voidcell = [tup for tup in void if tup not in projection(a,b,c,face)][0]
	cont = contaminated(voidcell,face.v)
	contcell = [p for p in pos if proj(p,face) == cont][0]# the contaminated cell
	return contcell


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
	return PosGroup(x0y0,'xy',(0,0)),PosGroup(x0y1,'xy',(0,1)),PosGroup(x1y0,'xy',(1,0)),PosGroup(x1y1,'xy',(1,1)),PosGroup(y0z0,'yz',(0,0)),PosGroup(y0z1,'yz',(0,1)),PosGroup(y1z0,'yz',(1,0)),PosGroup(y1z1,'yz',(1,1)),PosGroup(x0z0,'zx',(0,0)),PosGroup(x0z1,'zx',(1,0)),PosGroup(x1z0,'zx',(0,1)),PosGroup(x1z1,'zx',(1,1))
	
def projection(a,b,c,face):
	coord = face.c
	if coord == 'x':
		return [(a.y,a.z),(b.y,b.z),(c.y,c.z)]
	if coord == 'y':
		return [(a.z,a.x),(b.z,b.x),(c.z,c.x)]
	if coord == 'z':
		return [(a.x,a.y),(b.x,b.y),(c.x,c.y)]
	raise BaseException("Invalid Coordinate")

def proj(p,face):
	return projection(p,p,p,face)[0]
	
def contaminated(vc,value):
	""" returns the cell contaminated by the void cell"""
	if value:
		return trigo(vc)
	else:
		return horaire(vc)

def horaire(vc):
	""" rotation of vc in the clock direction """
	x,y = vc
	if x and y:
		return (1,0)
	elif x and not y:
		return 0,0
	elif not x and not y:
		return 0,1
	else:
		return 1,1

def trigo(vc):
	""" rotation in the trigonometric direction """
	x,y = horaire(vc); return not x, not y

def rotate_well(a,b,c,rot=None):
	""" computes all the required rotations """
	if rot == None:
		rot = []
	pos = a,b,c
	if [p for p in pos if p.x == 0 and p.y == 0 and p.z == 0]:
		if [p for p in pos if p.x == 0 and p.y == 0 and p.z]:
			if [p for p in pos if p.x == 0 and p.y == 1 and p.z == 0]:
				return a,b,c
	raise NotImplementedError

def rotate(pos,c,v):
	""" rotates according to a coordinate and a value """
	raise NotImplementedError
