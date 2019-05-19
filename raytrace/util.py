'''
This is a python util library for Ray Tracing written by Arthur Scardua
'''
import math
from copy import deepcopy

# tol error
EPSILON = 0.00001

class matrix:
    def __init__(self,matrix_list):
        self.m = len(matrix_list)
        self.n = len(matrix_list[0])
        
        for line in matrix_list:
            if len(line) != self.n:
                raise TypeError
        
        self.matrix_list = deepcopy(matrix_list)
    def inner_range(self,m,n):
        if (n>=self.n) or (m>=self.m):
            raise IndexError

    def __getitem__(self,pos):
        m,n = pos
        self.inner_range(*pos)
        return self.matrix_list[m][n] 

    def __setitem__(self,pos,data):
        m,n = pos
        self.inner_range(*pos)
        self.matrix_list[m][n] = data 

    def __eq__(self, other):
        if not isinstance(other, matrix):
            return False
        if (self.m != other.m) or (self.n != other.n):
            return False
        list_of_true = [abs(self[m,n] - other[m,n]) < EPSILON for n in range(self.n) for m in range(self.m)]
        return all(list_of_true)



class rtTuple():
    '''
    Ray tracing tuple (x,y,z,w). x,y and z are the position coordinates and w is
    related to pontins (0) and vectores (1).
    '''

    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def is_point(self):
        return self.w == 1

    def is_vector(self):
        return self.w == 0

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            assertion = abs(self.x - other.x) < EPSILON and\
                abs(self.y - other.y) < EPSILON and\
                abs(self.z - other.z) < EPSILON
            return assertion
        else:
            return False

    def __add__(self, other):
        return rtTuple(self.x+other.x, self.y+other.y, self.z+other.z, self.w +
                       other.w)

    def __sub__(self, other):
        return rtTuple(self.x-other.x, self.y-other.y, self.z-other.z, self.w -
                       other.w)

    def __abs__(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __mul__(self, other):
        return rtTuple(other * self.x, other * self.y, other * self.z, self.w)

    __rmul__ = __mul__

    def __neg__(self):
        return -1 * self

    def __truediv__(self, other):
        return rtTuple(self.x / other, self.y / other, self.z / other, self.w)


def point(x, y, z):
    return rtTuple(x, y, z, 1)


def vector(x, y, z):
    return rtTuple(x, y, z, 0)


def normalize(vec):
    return vec / abs(vec)


def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w


def cross(a, b):
    x = a.y * b.z - a.z * b.y
    y = a.z * b.x - a.x * b.z
    z = a.x * b.y - a.y * b.x
    return vector(x, y, z)


class color(rtTuple):
    def __init__(self, red, green, blue):
        super().__init__(red, green, blue, -2)
        self.red = self.x
        self.green = self.y
        self.blue = self.z

    @staticmethod
    def from_tuple(**kargs):
        return color(kargs['x'],kargs['y'],kargs['z'])

    def __add__(self, other):
        add_tuple = super().__add__(other).__dict__
        return self.from_tuple(**add_tuple)

    def __sub__(self, other):
        sub_tuple = super().__sub__(other).__dict__
        return self.from_tuple(**sub_tuple)

    def __mul__(self, other):
        if isinstance(other, color):
            return color(self.red * other.red, self.green * other.green,
                         self.blue * other.blue)
        else:
            mult_tuple = super().__mul__(other).__dict__
            return self.from_tuple(**mult_tuple)

    __rmul__ = __mul__
