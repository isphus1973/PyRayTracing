'''
This is a python util library for Ray Tracing written by Arthur Scardua
'''
import math
from copy import deepcopy

# tol error
EPSILON = 0.00001
TUPLE_SIZE = 4

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
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            new_matrix_list = [[other * element for element in line] for line
             in self.matrix_list]
            
            return matrix(new_matrix_list)
        elif isinstance(other, matrix):
            if other.n != self.m:
                raise ValueError('Matrix columns should match other lines')
            new_matrix_list = [
                [sum([self[i,k] * other[k,j] for k in range(self.n)]) for j in 
                range(other.n)] for i in range(self.m)
            ]
            return matrix(new_matrix_list)
        elif isinstance(other, rtTuple):
            if self.n != TUPLE_SIZE or self.m != TUPLE_SIZE:
                raise ValueError('matrix should have the rtTuple size')
            
            tuple_values = [other * rtTuple(*line) for line in self.matrix_list]

            return rtTuple(*tuple_values)
        else:
            raise NotImplementedError

    __rmul__ = __mul__

    def transpose(self):
        transposed_matrix_list = transpose(self).matrix_list
        self.__init__(transposed_matrix_list)

    def __str__(self):
        lines = ['|' + ' '.join([str(x) for x in line]) + '|' for line in self.matrix_list]
        return '\n'.join(lines)

    __repr__ = __str__


def transpose(mt):
    '''
    Transpose a matrix

    input a matrix and return a matrix
    '''
    if not isinstance(mt,matrix):
        raise TypeError('Expecting a matrix type input')

    matrix_input_list = mt.matrix_list

    matrix_output_list = [[matrix_input_list[n][m] for n in range(mt.n)] for m in range(mt.m)]

    return matrix(matrix_output_list)

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

    def __str__(self):
        return [self.x,self.y,self.z,self.w].__str__()

    __repr__ = __str__

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
        if isinstance(other, float) or isinstance(other, int):
            return rtTuple(other * self.x, other * self.y, other * self.z, self.w)
        elif isinstance(other, rtTuple):
            return other.x * self.x + other.y * self.y + other.z * self.z + other.w * self.w
        else:
            raise NotImplementedError

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

def identity_matrix_func(dim):
    identity_matrix_list = [[1 if x == y else 0 for x in range(dim)] for y in range(dim)]
    return matrix(identity_matrix_list)

identity_matrix = identity_matrix_func(4) 



