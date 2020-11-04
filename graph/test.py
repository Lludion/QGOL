# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:52:49 2020

@author: jmcos
"""

from qgol import *
from obj.base import *
from obj import *
from sys import argv
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def plot_cube(point,ax,alpha):
    
    cube_definition=[point]
    for i in range(3):
        pt=[j for j in point]
        pt[i]=pt[i]+1
        cube_definition.append(pt)
        
    cube_definition_array = [
        np.array(list(item))
        for item in cube_definition
    ]

    points = []
    points += cube_definition_array
    vectors = [
        cube_definition_array[1] - cube_definition_array[0],
        cube_definition_array[2] - cube_definition_array[0],
        cube_definition_array[3] - cube_definition_array[0]
    ]

    points += [cube_definition_array[0] + vectors[0] + vectors[1]]
    points += [cube_definition_array[0] + vectors[0] + vectors[2]]
    points += [cube_definition_array[0] + vectors[1] + vectors[2]]
    points += [cube_definition_array[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]


    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    faces.set_facecolor((1-(alpha/2),0,0,alpha))

    ax.add_collection3d(faces)


    # Plot the points themselves to force the scaling of the axes
    ax.scatter(points[:,0], points[:,1], points[:,2], s=0)

    #ax.set_aspect('equal')
    
    
def Fusion(qgol):
    dic =defaultdict(float)
    for conf,alpha in qgol.s.cs.items():
        for cell in conf.tuple():
            dic[cell]+=abs(alpha)*abs(alpha)
    return dic

def Afficher_qgol(qgol):
    dic= Fusion(qgol)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    for point,alpha in dic.items():
        plot_cube(point, ax,alpha)
    return
    
qgol=QGOL()
qgol.bc[0,0,0] = Cell(True)
qgol.bc[1,0,0] = Cell(True)
qgol.bc[0,1,0] = Cell(True)
qgol.next()



#Qgol2listcube(qgol)
Afficher_qgol(qgol)


