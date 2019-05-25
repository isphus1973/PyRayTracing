'''
This file test the matrix class
'''

import unittest
from raytrace.util import matrix, rtTuple, identity_matrix, transpose

class testMatrix(unittest.TestCase):
    'This tests the matrix class'

    def test_matrix_creation(self):

        matrix_list = [
            [1,2,3,4],
            [5.5,6.5,7.5,8.5],
            [9,10,11,12],
            [13.5,14.5,15.5,16.5]
        ]
        M = matrix(matrix_list)

        self.assertEqual(M[0,0],1,'The component (0,0) should be 1')
        self.assertEqual(M[0,3],4,'The component (0,3) should be 4')
        self.assertEqual(M[1,0],5.5,'The component (1,0) should be 5.5')
        self.assertEqual(M[1,2],7.5,'The component (1,2) should be 7.5')
        self.assertEqual(M[2,2],11,'The component (2,2) should be 11')
        self.assertEqual(M[3,0],13.5,'The component (3,0) should be 13.5')
        self.assertEqual(M[3,2],15.5,'The component (3,2) should be 15.5')
    
    def test_matrix_eq(self):

        matrix_list = [
            [1,2,3,4],
            [5.5,6.5,7.5,8.5],
            [9,10,11,12],
            [13.5,14.5,15.5,16.5]
        ]
        M1 = matrix(matrix_list)
        M2 = matrix(matrix_list)
        
        self.assertEqual(M1,M2,'The both matrices should be equal')
        M2[0,3] = 77
        self.assertFalse(M1[0,3]==77, 'The component (0,7) should not be 77')
        self.assertFalse(M1 == M2, 'These matrices should be different')

    def test_matrix_multiplication(self):
        '''
        TODO: 
            - scalar multiplication
            - matrix multiplication
            - tuple multiplication
        '''
        matrix_list = [
            [1,2,3,4],
            [5.5,6.5,7.5,8.5],
            [9,10,11,12],
            [13.5,14.5,15.5,16.5]
        ]

        matrix_list2 = [
            [2,4,6,8],
            [11,13,15,17],
            [18,20,22,24],
            [27,29,31,33]
        ]

        M1 = matrix(matrix_list)
        M2 = matrix(matrix_list2)
        scalar1 = 2

        self.assertEqual(scalar1 * M1 , M2, 'This multiplication should word')

        matrix_list_A = [
            [1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]
        ]

        matrix_list_B = [
            [-2,1,2,3],
            [3,2,1,-1],
            [4,3,6,5],
            [1,2,7,8]
        ]

        matrix_list_AB = [
            [20,22,50,48],
            [44,54,114,108],
            [40,58,110,102],
            [16,26,46,42]
        ]

        Ma = matrix(matrix_list_A)
        Mb = matrix(matrix_list_B)
        Mc = matrix(matrix_list_AB)

        self.assertEqual(Ma * Mb, Mc, 'This multiplication should be equal')

        matrix_list_t = [
            [1,2,3,4],
            [2,4,4,2],
            [8,6,4,1],
            [0,0,0,1]
        ]

        Mt = matrix(matrix_list_t)
        tuple_input = rtTuple(1,2,3,1)
        tuple_output = rtTuple(18,24,33,1)

        self.assertEqual(Mt * tuple_input, tuple_output, 'this should be a tuple')

    def test_identity_matrix(self):

        matrix_list = [
            [0,1,2,4],
            [1,2,4,8],
            [2,4,8,16],
            [4,8,16,32]
        ]

        Mt = matrix(matrix_list)

        self.assertEqual(identity_matrix * Mt, Mt, 'The identity should not alter the Matrix')

        tuple_list = [1,2,3,4]

        Tt = rtTuple(*tuple_list)

        self.assertEqual(identity_matrix * Tt, Tt, 'The identity should not alter the tuple')

    def test_transpose_matrix(self):

        matrix_list = [
            [0,9,3,0],
            [9,8,0,8],
            [1,8,5,3],
            [0,0,5,8]
        ]

        matrix_transposed_list = [
            [0,9,1,0],
            [9,8,8,0],
            [3,0,5,5],
            [0,8,3,8]
        ]

        Mt = matrix(matrix_list)
        Mt_transposed = matrix(matrix_transposed_list)

        self.assertEqual(transpose(Mt),Mt_transposed,'The matrix transposed is failing')
        Mt.transpose()
        self.assertEqual(Mt,Mt_transposed,'The matrix transposed inplace method is failing')
        
        self.assertEqual(transpose(identity_matrix),identity_matrix\
            , 'The transposition of the identity should be the identity')
