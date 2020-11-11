# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:52:49 2020

@author: jmcos, lludion
"""

from qgol import *
from obj import *
from img.display import *
from hypothesis import given,settings
from random import randint
import hypothesis.strategies as st
from os import environ

@given(st.integers(2,10),st.integers(2,3),st.integers(1,3),st.integers(1,3))
@settings(max_examples=50,deadline=750)
def test_unitary(n,xmax,ymax,zmax):
    """ tests on lots of randomized examples if figure calculation:
        - is fast enough
        - contains no errors """
    qgol = QGOL()
    qgol.bc[0,0,0] = Cell(True)
    qgol.bc[1,0,0] = Cell(True)
    qgol.bc[0,1,0] = Cell(True)
    for i in range(n):
        x = randint(0,xmax)
        y = randint(0,ymax)
        z = randint(0,zmax)
        qgol.bc[x,y,z] = Cell(True)
    qgol.next()
    
    afficher_qgol(qgol,False)



def test_show(n=30,xmax=5,ymax=5,zmax=5,show=True):
    """ tests if figure calculation contains no errors, then shows it. """
    qgol = QGOL()
    qgol.bc[0,0,0] = Cell(True)
    qgol.bc[1,0,0] = Cell(True)
    qgol.bc[0,1,0] = Cell(True)
    qgol.bc[0,0,1] = Cell(True)
    
    for i in range(n):
        x = randint(-xmax,xmax)
        y = randint(-xmax,ymax)
        z = randint(-xmax,zmax)
        qgol.bc[x,y,z] = Cell(True)
     
    #Qgol2listcube(qgol)
    qgol.next()

    afficher_qgol(qgol,"PYTEST_CURRENT_TEST" not in environ)

