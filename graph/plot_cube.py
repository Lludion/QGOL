"""
@author: jmcos, lludion
"""

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def plot_cube(point,ax,alpha,index_color):
    """ Plots a cube in the position 'point', with amplitude alpha """
    alpha=round(alpha,3)
    
    list_color=[[1,0,0],[0,1,0],[0,0,1],[0.5,0.5,0],[0.5,0,0.5],[0,0.5,0.5],[0.33,0.33,0.33],[0.25,0.25,0.5]]
    color = list_color[index_color]
    
    
    cube_definition = [point]
    for i in range(3):
        pt = [j for j in point]
        pt[i] = pt[i]+1
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
    
    #Calculate the colors of the cube
    new_color=[0,0,0]
    for i in range(3):
        if(color[i]!=0):
            new_color[i]=round(color[i]-color[i]*(alpha/2),3)
            

    faces.set_facecolor((new_color[0],new_color[1],new_color[2],alpha))

    ax.add_collection3d(faces)


    # Plot the points themselves to force the scaling of the axes
    ax.scatter(points[:,0], points[:,1], points[:,2], s=0)

    #ax.set_aspect('equal')

