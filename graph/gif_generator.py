# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:37:15 2020

@author: jmcos
"""

from qgol import *
from obj import *
from graph.display import *
from os import environ

def generer_gif(l):
    return

qgol = QGOL()
qgol.bc[0,0,0] = Cell(True)
qgol.bc[1,0,0] = Cell(True)
qgol.bc[0,1,0] = Cell(True)
qgol.bc[4,4,4] = Cell(True)
qgol.bc[5,5,5] = Cell(True)

qgol.next()
afficher_qgol(qgol,"PYTEST_CURRENT_TEST" not in environ)