'''
This is a python test for  tupĺe library
for Ray Tracing written by Arthur Scardua
'''

import unittest
import math
from raytrace.util import rtTuple, point, vector, normalize, dot, cross


class testTuple(unittest.TestCase):
    '''
    Test the rtTuple class
    '''

    def test_tuple_point(self):

        ap = rtTuple(4.3, -4.2, 3.1, 1)
        ap2 = rtTuple(4.3, -4.2, 3.1, -1)

        self.assertNotEqual( ap, ap2, 'These tuples should not be equal')
        self.assertEqual(ap.x, 4.3, 'x should be 4.3')
        self.assertEqual(ap.y, -4.2, 'y should be -4.2')
        self.assertEqual(ap.z, 3.1, 'z should be 3.1')
        self.assertEqual(ap.w, 1, 'w should be 1')

        self.assertTrue(ap.is_point(), 'This should be a point')
        self.assertFalse(ap.is_vector(), 'This should not be a vector')

    def test_tuple_vector(self):

        av = rtTuple(4.3, -4.2, 3.1, 0)

        self.assertEqual(av.x, 4.3, 'x should be 4.3')
        self.assertEqual(av.y, -4.2, 'y should be -4.2')
        self.assertEqual(av.z, 3.1, 'z should be 3.1')
        self.assertEqual(av.w, 0, 'w should be 0')

        self.assertFalse(av.is_point(), 'This should not be a point')
        self.assertTrue(av.is_vector(), 'This should be a vector')

    def test_function_point(self):
        ap = point(1, 1, 1)
        atuple = rtTuple(1, 1, 1, 1)
        self.assertEqual(ap, atuple, 'This should be a point')

    def test_function_vector(self):
        av = vector(1, 1, 1)
        atuple = rtTuple(1, 1, 1, 0)
        scalar = math.sqrt(3)
        self.assertEqual(av, atuple, 'This should be a point')
        self.assertEqual(abs(av), scalar, 'The abs value should be {scalar}')

    def test_tuple_general(self):

        ap = point(1.1, 4.5, 4.6)
        av = vector(0, 2.1, 3.3)
        ap2 = point(1.1, 6.6, 7.9)
        av2 = vector(1, 2, 3)
        av3 = vector(1, -0.1, -0.3)
        ap3 = point(-1.1, -4.5, -4.6)

        self.assertEqual(av + av3, av2, 'These shoud be equal')
        self.assertEqual(ap + av, ap2, 'These shoud be equal')
        self.assertEqual(ap2-ap, av, 'These should be equal')
        self.assertEqual(ap2-av, ap, 'These should be equal')
        self.assertEqual(av2-av, av3, 'These should be equal')
        self.assertEqual(-ap, ap3, 'These should be equal')

        #multiplication and division
        ascalar = 3.5
        ascalar2 = 0.5
        scalar3 = 2
        ap = point(1, 2, 4.4)
        ap2 = point(3.5, 7, 15.4)
        ap3 = point(0.5, 1, 2.2)

        self.assertEqual(ascalar * ap, ap2,
                         'This multiplication should be equal')
        self.assertEqual(ascalar2 * ap, ap3,
                         'This multiplication should be equal')
        self.assertEqual(ap / scalar3, ap3, 'This division shouldbe equal')

    def test_norm_vectors(self):

        av = vector(4, 0, 0)
        av2 = vector(1, 2, 3)
        av3 = vector(0.26726, 0.53452, 0.80178)
        av4 = vector(1, 0, 0)

        self.assertEqual(normalize(av), av4,
                         'The normalization should be (1,0,0)')
        self.assertEqual(normalize(av2), av3,
                         'The normalization should be (0.26726, 0.53452, 0.80178)')
        self.assertEqual(abs(normalize(av2)), 1,
                         'The normalized vector shoud be 1')

    def test_dot_product(self):

        a = vector(1, 2, 3)
        b = vector(2, 3, 4)

        self.assertEqual(dot(a, b), 20, 'The dot product should be equal 20')
        self.assertEqual(dot(b, a), 20, 'The dot product should be equal 20')

    def test_cross_product(self):

        a = vector(1, 2, 3)
        b = vector(2, 3, 4)

        self.assertEqual(cross(a, b), vector(-1, 2, -1),
                         'This cros product should be (-1,2,-1)')
        self.assertEqual(cross(b, a), vector(1, -2, 1),
                         'This cros product should be (1,-2,1)')


if __name__ == '__main__':
    unittest.main()
