# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:37:15 2020

@author: jmcos
"""

from qgol import *
from obj import *
from graph.display import *
from os import environ


#Autoscale permet de fixer automatiquement une échelle adaptée
#Si on ne précise ni la valeur de autoscale ni la valeur de scale 
#l'échelle est "dynamique"
def generer_gif(qgol,nb_step,name,scale=(0,0,0),autoscale=False):
    if autoscale:
        copy = qgol.copy()
        for i in range(nb_step):
            copy.next()
        scl=afficher_qgol(copy,show=False,save=name+"copy")
    else:
        scl=scale
    
    if scale[0]==0:
        for i in range(nb_step):
            afficher_qgol(qgol,show=False,save=name+"%d" %i)
            qgol.next()
        
    else:
        for i in range(nb_step):
            afficher_qgol(qgol,show=False,save=name+"%d" %i,scale=scl)
            qgol.next()
    return

qgol = QGOL()
qgol.bc[0,0,0] = Cell(True)
qgol.bc[1,0,0] = Cell(True)
qgol.bc[0,1,0] = Cell(True)
qgol.bc[3,4,4] = Cell(True)
qgol.bc[3,5,5] = Cell(True)
qgol.bc[3,3,1] = Cell(True)

    
generer_gif(qgol,10, "test")

