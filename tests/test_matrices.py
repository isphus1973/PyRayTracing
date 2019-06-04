'''
This file test the matrix class
'''

import unittest
from raytrace.util import matrix, rtTuple, identity_matrix, transpose, det, submatrix, minor, cofactor, inverse

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

class testMatrixOperations(unittest.TestCase):
    '''
    Test operations that acts over matrices such as transformations and determinant
    '''

    def test_determinant_2x2(self):

        matrix_list = [
                [1,5],
                [-3,2]
                ]

        Mt = matrix(matrix_list)

        self.assertEqual( det(Mt), 17, 'The determinant should be 17')

    def test_submatrix_3x3(self):

        matrix_list = [
                [1,5,0],
                [-3,2,7],
                [0,6,-3]
                ]

        matrix_list_output = [
                [-3,2],
                [0,6]
                ]

        Mt = matrix(matrix_list)
        Mt_output = matrix(matrix_list_output)

        self.assertEqual( submatrix(Mt,0,2), Mt_output, 'The submatrix of a 3x3 matrix failed')

    def test_submatrix_4x4(self):

        matrix_list_input = [
                [-6,1,1,6],
                [-8,5,8,6],
                [-1,0,8,2],
                [-7,1,-1,1]
            ]

        matrix_list_output = [
                [-6,1,6],
                [-8,8,6],
                [-7,-1,1]
            ]

        Mt = matrix(matrix_list_input)
        Mt_output = matrix(matrix_list_output)

        self.assertEqual( submatrix(Mt, 2, 1), Mt_output, 'The submatrix of a 4x4 matrix failed')

    
    def test_minor(self):

        matrix_list = [
                [3,5,0],
                [2,-1,-7],
                [6,-1,5]
            ]

        Mt = matrix(matrix_list)
        Mt_submatrix = submatrix(Mt, 1, 0)

        self.assertEqual( det(Mt_submatrix), 25, 'The 3x3 submatrix determinant failed')
        self.assertEqual( minor(Mt, 1, 0), 25, 'The minor of 3x3 matrix failed')

    def test_cofactor(self):

        matrix_list = [
                [3,5,0],
                [2,-1,-7],
                [6,-1,5]
            ]

        Mt = matrix(matrix_list)

        self.assertEqual( minor(Mt, 0, 0), -12, 'The matrix minor failed')
        self.assertEqual( cofactor(Mt, 0, 0), -12, 'The matrix cofactor failed')
        self.assertEqual( minor(Mt, 1,0), 25, 'The matrix minow failed')
        self.assertEqual( cofactor(Mt, 1, 0), -25, 'The matrix cofactor failed')

    def test_determinant_3x3(self):

        matrix_list = [
                [1,2,6],
                [-5,8,-4],
                [2,6,4]
            ]

        Mt = matrix(matrix_list)

        self.assertEqual( cofactor(Mt,0,0), 56, 'The cofactor of 3x3 matrix failed')
        self.assertEqual( cofactor(Mt,0,1), 12, 'The cofactor of 3x3 matrix failed')
        self.assertEqual( cofactor(Mt,0,2), -46, 'The cofactor of 3x3 matrix failed')

        self.assertEqual( det(Mt), -196, 'The determinant of 3x3 matrix failed')

    def test_determinant_4x4(self):

        matrix_list = [
                [-2,-8,3,5],
                [-3,1,7,3],
                [1,2,-9,6],
                [-6,7,7,-9]
            ]

        Mt = matrix(matrix_list)

        self.assertEqual( cofactor(Mt,0,0), 690, 'The cofactor of 4x4 failed')
        self.assertEqual( cofactor(Mt,0,2), 210, 'The cofactor of 4x4 failed')
        self.assertEqual( cofactor(Mt,0,3), 51, 'The cofactor of 4x4 failed')
        self.assertEqual( cofactor(Mt,0,1), 447, 'The cofactor of 4x4 failed')

        self.assertEqual( det(Mt), -4071, 'The determinant of 4x4 matrix failed')

class testMatrixInversion(unittest.TestCase):

    def test_invertible_4x4(self):

        matrix_list = [
                [6,4,4,4],
                [5,5,7,6],
                [4,-9,3,-7],
                [9,1,7,-6]
            ]

        Mt = matrix(matrix_list)

        self.assertEqual( det(Mt), -2120, 'The 4x4 matrix determinant failed')
        self.assertTrue( Mt.is_inv(), 'The matrix should be invertible')

    def test_not_invertible_4x4(self):

        matrix_list = [
                [-4,2,-2,-3],
                [9,6,2,6],
                [0,-5,1,-5],
                [0,0,0,0]
            ]

        Mt = matrix(matrix_list)

        self.assertEqual( det(Mt), 0, 'The 4x4 matrix null determinant failed')
        self.assertFalse( Mt.is_inv(), 'The matrix should not be invertible')

    def test_inversion(self):

        matrix_list = [
                [-5,2,6,-8],
                [1,-5,1,8],
                [7,7,-6,-7],
                [1,-3,7,4]
            ]


        matrix_list_inverse = [
                [0.21805, 0.45113, 0.24060, -0.04511],
                [-0.80827, -1.45677, -0.44361, 0.52068],
                [-0.07895, -0.22368, -0.05263, 0.19737],
                [-0.52256, -0.81391, -0.30075, 0.30639]
            ]
    
        Mt = matrix(matrix_list)
        Mt_inverse = inverse(Mt)
        Mt_inverse_output = matrix(matrix_list_inverse)

        self.assertEqual( det(Mt), 532, 'The determinant of 4x4 matrix failed')
        
        self.assertEqual( cofactor(Mt, 2, 3), -160, 'The cofactor of 4x4 matrix failed')
        self.assertEqual( Mt_inverse[3,2], -160/532, 'The inverse element failed')

        self.assertEqual( cofactor(Mt, 3, 2), 105, 'The cofactor of 4x4 matrix failed')
        self.assertEqual( Mt_inverse[2,3], 105/532, 'The inverse element failed')
        
        self.assertEqual( Mt_inverse, Mt_inverse_output, 'The 4x4 inverse failed')

    def test_inversion2(self):

        matrix_list1 = [
                [ 8, -5,  9,  2 ],
                [ 7,  5,  6,  1 ],
                [-6,  0,  9,  6 ],
                [-3,  0, -9, -4 ]
            ]

        matrix_list1_inv = [
                [-0.15385, -0.15385, -0.28205, -0.53846 ],
                [-0.07692,  0.12308,  0.02564,  0.03077 ],
                [ 0.35897,  0.35897,  0.43590,  0.92308 ],
                [-0.69231, -0.69231, -0.76923, -1.92308 ]
            ]

        Mt1 = matrix(matrix_list1)
        Mt_inverse1 = inverse(Mt1)
        Mt_inverse1_output = matrix(matrix_list1_inv)

        self.assertEqual( Mt_inverse1, Mt_inverse1_output, 'The inverse of 4x4 matrix failed')

    def test_inversion3(self):

        matrix_list = [
                [ 9,  3,  0,  9 ],
                [-5, -2, -6, -3 ],
                [-4,  9,  6,  4 ],
                [-7,  6,  6,  2 ]
            ]

        matrix_list_inv = [
                [-0.04074, -0.07778,  0.14444, -0.22222 ],
                [-0.07778,  0.03333,  0.36667, -0.33333 ],
                [-0.02901, -0.14630, -0.10926,  0.12963 ],
                [ 0.17778,  0.06667, -0.26667,  0.33333 ]
            ]

        Mt = matrix(matrix_list)
        Mt_inverse = inverse(Mt)
        Mt_inverse_output = matrix(matrix_list_inv)

        self.assertEqual( Mt_inverse, Mt_inverse_output, 'The inverse of 4x4 matrix failed')

    def test_inverse_multiplication(self):

        matrix_list_A = [
                [ 3,-9, 7, 3 ],
                [ 3,-8, 2,-9 ],
                [-4, 4, 4, 1 ],
                [-6, 5,-1, 1 ]
            ]

        matrix_list_B = [
                [ 8, 2, 2, 2 ],
                [ 3,-1, 7, 0 ],
                [ 7, 0, 5, 4 ],
                [ 6,-2, 0, 5 ]
            ]

        MtA = matrix(matrix_list_A)
        MtB = matrix(matrix_list_B)

        MtC = MtA * MtB

        self.assertEqual( MtC * inverse(MtB), MtA, 'Inverse multiplication failed')

        self.assertEqual
