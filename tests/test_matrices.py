'''
This file test the matrix class
'''

import unittest
from raytrace.util import matrix

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


