from raytrace.util import *
matrix_list = [
    [0,9,3,0],
    [9,8,0,8],
    [1,8,5,3],
    [0,0,5,8]
]

matrix_transposed_list = [
    [0,9,1,9],
    [9,8,8,0],
    [3,0,5,5],
    [0,8,3,8]
]

Mt = matrix(matrix_list)
Mt_transposed = matrix(matrix_transposed_list)

print(Mt)
print('----------')
print(Mt_transposed)
print('----------')
print(transpose(Mt))

print(rtTuple(1,2,3,4))