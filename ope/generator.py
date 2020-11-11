""" Generation of quantum doors in a configuration (of Econfig type) 

It is assumed that each door is built so that the qubit only ever goes to the right (x only increases) 

Initially, x,y,z = 000 for the qubit.

"""
from ope.doors import *

def parsedoors(txt):
	""" takes a text description of a list of doors as an input, returns the list of doors
	
	Hadamard door : char h (not working)
	R (pi/4) door : char 4
	cR (pi/4) door : char c (not working)
	"""
	li = []
	for a in txt:
		if a == 'H' or a == 'h':
			li.append('h')
		elif a == 'c' or a == 'C':
			li.append('c')
		elif a == '4' or a == 'r':
			li.append('4')
	return li

def doorify(conf,txt):
	doors = parsedoors(txt)
	crpi4 = Crpi4()
	rpi4 = Rpi4()
	hadamard = Hadamard()
	posdors = [rpi4,crpi4,hadamard] # possible doors
	pointers = [(0,0,0)]
	gs = 0 #generated steps
	for d in doors:
		s2,outposts = [door.generate(gs,conf,pointers,[]) for door in posdors if door.id == d][0]
		print("Hour of Impact : ",s2,"Position after impact:",outposts)
		pointers = outposts 
		gs = s2


