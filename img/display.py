"""
@author: jmcos, lludion
"""

from img.plot_cube import plot_cube
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import cmath as comp
import math as mt
from os import path,makedirs

def fusion(qgol):
    """ Calculates a config from a superposition, by adding the amplitudes. """
    amplitude = defaultdict(float)
    vec_0 = lambda:[0,0,0,0,0,0,0,0]
    color = defaultdict(vec_0)
    for conf,alpha in qgol.s.cs.items():
        for cell in conf.tuple():
            amplitude[cell] += abs(alpha)*abs(alpha)
            phase = int((comp.phase(alpha)/(2*mt.pi))*8)%8
            vec = color[cell]
            vec[phase] += (abs(alpha)*abs(alpha))
            color[cell] = vec
    for cell,v in color.items():
        color[cell] = np.argmax(v)
    return amplitude,color


def afficher_qgol(qgol,show=False,save='',scale=(0,0,0)):
    """ Plots the qgol if show is true.
    Else, only calculates the figure, then clears it. """
    amplitude,color = fusion(qgol)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.set_axis_off()
    for point,alpha in amplitude.items():
        plot_cube(point, ax,alpha,color[point])
    if(scale[0]!=0):
        ax.set_xlim(scale[0])
        ax.set_ylim(scale[1])
        ax.set_zlim(scale[2])
    if show: return plt.show()
    if len(save) > 0:
        if not isinstance(save,str):
        	save = str(save)
        filename = path.join("img","gif",save + ".jpg")
        makedirs(path.dirname(filename), exist_ok=True) #os function
        plt.savefig(filename)
        return (ax.get_xlim(),ax.get_ylim(),ax.get_zlim())
    else: 
        plt.clf()
        plt.clf()
        plt.cla()
        plt.close()

