"""
@author: jmcos, lludion
"""

from graph.plot_cube import plot_cube
from collections import defaultdict
import matplotlib.pyplot as plt

def fusion(qgol):
    """ Calculates a config from a superposition, by adding the amplitudes. """
    dic = defaultdict(float)
    for conf,alpha in qgol.s.cs.items():
        for cell in conf.tuple():
            dic[cell] += abs(alpha)*abs(alpha)
    return dic

def afficher_qgol(qgol,show=False):
    """ Plots the qgol if show is true.
    Else, only calculates the figure, then clears it. """
    dic = fusion(qgol)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_axis_off()
    for point,alpha in dic.items():
        plot_cube(point, ax,alpha)
    if show: return plt.show()
    else: 
        plt.clf()
        plt.clf()
        plt.cla()
        plt.close()

