""" Operations on a configuration """

def fullcube(c,p,n=2,act=True,show=True):
	""" activates a full cube of size n, beginning in position p 
	for instance, with n = 2, it will activate
	p.x + 1/2 +- 1/2,p.y + 1/2 +- 1/2,p.z + 1/2 +- 1/2
	
	if act is not True, is deactivates all the cells
	"""
	x,y,z = p.xyz()
	msk = []
	if act:
		for i in range(n):
			for j in range(n):
				for k in range(n):
					c[x+i,y+j,z+k].activate()
					if not show:
						msk.append((x+i,y+j,z+k))
	else:
		for i in range(n):
			for j in range(n):
				for k in range(n):
					c[x+i,y+j,z+k].deactivate()
	return msk

def tunnelx(c,p,n=2,show=False):
	"""
	keep in mind that for the tunnel to work, it should begin accordingly with the cubes
	"""
	x,y,z = p.xyz()
	msk= []
	for i in range(n):
		for j in range(4):
			for k in range(4):
				if ((j%3) or (k%3)) and not ((j%3) and  (k%3)):
					c[x+i,y+j,z+k].activate()
					if not show:msk.append((x+i,y+j,z+k))
	return msk

	

