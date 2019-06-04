'''
This is the matrix transformation module for raytracing written by
Arthur Scardua
'''

from raytrace.util import matrix
from math import cos, sin

def translation(x,y,z):
    '''
    3D translation linear operator

    translation(x,y,z)

    Translate a point or vector to a new place
    
    Parameters
    ----------

    -x (float): x position
    -y (float): y position
    -z (float): z position

    Return
    ------

    -matrix: A matrix that transforms a vector or point
    '''

    matrix_list = [
            [1,0,0,x],
            [0,1,0,y],
            [0,0,1,z],
            [0,0,0,1]
        ]

    return matrix(matrix_list)

def scaling(x,y,z):
    '''
    3D scaling

    scaling(x,y,z)

    Scale a vector or a point. Reflection included.

    Parameters
    ----------

    -x (float): x scaling
    -y (float): y scaling
    -z (float): z scaling

    Return
    ------

    -matrix: A matrix that transforms a vector or point
    '''

    matrix_list = [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1]
        ]

    return matrix(matrix_list)

def rotation_x(ang):
    '''
    Left handed rotation around x axis.

    rotation_x(ang)

    Left handed rotation around x axis (angle in radians)
    
    Parameters
    ----------
    
    -ang (float): angle in radians

    Return
    ------

    -matrix: A rotation matrix
    '''

    cos_f = cos(ang)
    sin_f = sin(ang)

    matrix_list = [
            [1,0,0,0],
            [0, cos_f, -sin_f, 0],
            [0, sin_f, cos_f, 0],
            [0, 0, 0, 1]
        ]

    return matrix(matrix_list)


def rotation_y(ang):
    '''
    Left handed rotation around y ayis.

    rotation_y(ang)

    Left handed rotation around y ayis (angle in radians)
    
    Parameters
    ----------
    
    -ang (float): angle in radians

    Return
    ------

    -matrix: A rotation matrix
    '''

    cos_f = cos(ang)
    sin_f = sin(ang)

    matrix_list = [
            [cos_f, 0, sin_f, 0],
            [0, 1, 0, 0],
            [-sin_f, 0, cos_f, 0],
            [0, 0, 0, 1]
        ]

    return matrix(matrix_list)

def rotation_z(ang):
    '''
    Left handed rotation around z azis.

    rotation_z(ang)

    Left handed rotation around z azis (angle in radians)
    
    Parameters
    ----------
    
    -ang (float): angle in radians

    Return
    ------

    -matrix: A rotation matrix
    '''

    cos_f = cos(ang)
    sin_f = sin(ang)

    matrix_list = [
            [cos_f, -sin_f, 0, 0],
            [sin_f, cos_f, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

    return matrix(matrix_list)


def shearing(xy=0,xz=0,yx=0,yz=0,zx=0,zy=0):
    '''
    Shear transformation.
    
    shearing(xy=0,xz=0,yx=0,yz=0,zx=0,zy=0)

    Return a shear matrix for 3D points and vectors.

    Parameters
    ----------

    -xy (float): shear in xy direction
    -xz (float): shear in xz direction
    -yx (float): shear in yx direction
    -yz (float): shear in yz direction
    -zx (float): shear in zx direction
    -zy (float): shear in zy direction

    Return
    ------

    -matrix: return a shear matrix
    '''

    matrix_list = [
            [1, xy, xz, 0],
            [yx, 1, yz, 0],
            [zx, zy, 1, 0],
            [0, 0, 0, 1]
        ]

    return matrix(matrix_list)

