# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:37:15 2020

@author: jmcos
"""

from qgol import *
from obj import *
from graph.display import *
from os import environ

def generer_gif(qgol,nb_step,name,scale=(0,0,0)):
    if scale[0]==0:
        copy = qgol.copy()
        for i in range(nb_step):
            copy.next()
        scl=afficher_qgol(copy,show=False,save=name+"copy")
    else:
        scl=scale
    for i in range(nb_step):
        afficher_qgol(qgol,show=False,save=name+"%d" %i,scale=scl)
        qgol.next()
    return

qgol = QGOL()
qgol.bc[0,0,0] = Cell(True)
qgol.bc[1,0,0] = Cell(True)
qgol.bc[0,1,0] = Cell(True)
qgol.bc[4,4,4] = Cell(True)
qgol.bc[5,5,5] = Cell(True)

    
generer_gif(qgol,10, "test")

