"""A library of simple geometrical functions
"""

from math import sin, cos, pi


def nGon(centre, radius, n_sides):
    """returns vertices of a regular polygon as a list of 3D points as lists 
    input:
        centre - coordinate of centre-point as a list of three coordinates
        radius - radius of vertices from centre as float
        n_sides - number of vertices as an integer >3
    """
    x, y, z = centre
    n_s = max(n_sides, 3)
    angles = [2 * pi * i / n_s for i in range(0,int(n_s))]
    list_of_points = [(x + radius * cos(ang), y + radius * sin(ang), z) for ang in angles]
    return list_of_points  # e.g. [[2.4, 5.5, 3,8],[2.7, 5.4, 3,8],[...]]

