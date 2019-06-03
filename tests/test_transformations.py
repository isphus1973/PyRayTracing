'''
This is the test for the transformations module
'''

import unittest
from raytrace.util import point, inverse, vector
from raytrace.transformation import translation, scaling, rotation_x, rotation_y, rotation_z, shearing
from math import pi, sqrt

class testTransformations(unittest.TestCase):
    
    def test_translation(self):
        
        transform = translation(5,-3,2)

        p = point(-3,4,5)

        p_out = point(2,1,7)

        self.assertEqual( transform * p , p_out, 'The translation failed')


    def test_inv_translation(self):

        transform = translation(5,-3,2)

        inv = inverse(transform)

        p = point(-3,4,5)

        p_out = point(-8,7,3)

        self.assertEqual(inv * p, p_out, 'The inverse translation failed')


    def test_translation_vector(self):

        transform = translation(5,-3,2)

        v = vector(-3,4,5)

        self.assertEqual( transform * v, v, 'The translation of a vector failed')


    def test_scaling(self):

        transform = scaling(2,3,4)

        p = point(-4,6,8)

        p_out = point(-8,18,32)

        self.assertEqual( transform * p, p_out, 'The scaling of point fail')


    def test_scaling_vector(self):

        transform = scaling(2,3,4)

        v = vector(-4,6,8)

        v_out = vector(-8,18,32)

        self.assertEqual( transform * v , v_out, 'The scaling of vector failed')

    def test_inverse_scaling(self):

        transform = scaling(2,3,4)

        inv = inverse(transform)

        v = vector(-4,6,8)

        v_out =vector(-2,2,2)

        self.assertEqual( inv * v, v_out, 'The inverse scaling failed')


    def test_reflection(self):

        transform = scaling(-1,1,1)

        p = point(2,3,4)

        p_out = point(-2,3,4)

        self.assertEqual( transform * p, p_out, 'The reflection failed')

    def test_rotation_x(self):

        p = point(0,1,0)

        half_quarter = rotation_x(pi/4)
        full_quarter = rotation_x(pi/2)
        half_quarter_inv = inverse(half_quarter)

        p_out_half = point(0,sqrt(2)/2, sqrt(2)/2)
        p_out_full = point(0,0,1)
        p_out_inv = point(0, sqrt(2)/2, -sqrt(2)/2)

        self.assertEqual(half_quarter * p, p_out_half, 'x rotation failed')
        self.assertEqual( full_quarter * p, p_out_full, 'x rotation failed')
        self.assertEqual( half_quarter_inv  * p, p_out_inv, 'x inverse rotation failed')

    def test_rotation_y(self):

        p = point(0,0,1)

        half_quarter = rotation_y(pi/4)
        full_quarter = rotation_y(pi/2)

        p_out_half = point(sqrt(2)/2,0, sqrt(2)/2)
        p_out_full = point(1,0,0)

        self.assertEqual(half_quarter * p, p_out_half, 'y rotation failed')
        self.assertEqual( full_quarter * p, p_out_full, 'y rotation failed')

    def test_rotation_z(self):

        p = point(0,1,0)

        half_quarter = rotation_z(pi/4)
        full_quarter = rotation_z(pi/2)

        p_out_half = point(-sqrt(2)/2, sqrt(2)/2, 0)
        p_out_full = point(-1,0,0)

        self.assertEqual(half_quarter * p, p_out_half, 'z rotation failed')
        self.assertEqual( full_quarter * p, p_out_full, 'z rotation failed')

    
    def test_shearing_xy(self):

        transform = shearing(xy=1)

        p = point(2,3,4)

        p_out = point(5,3,4)

        self.assertEqual( transform * p, p_out, 'shearing in xy direction failed')


    def test_shearing_xz(self):

        transform = shearing(xz=1)

        p = point(2,3,4)

        p_out = point(6,3,4)

        self.assertEqual( transform * p, p_out, 'Shearing in xz direction failed')


    def test_shearing_yx(self):

        transform = shearing(yx=1)

        p = point(2,3,4)

        p_out = point(2,5,4)

        self.assertEqual( transform * p, p_out, 'Shearing in yx direction failed')

    def test_shearing_yz(self):

        transform = shearing(yz=1)

        p = point(2,3,4)

        p_out = point(2,7,4)

        self.assertEqual( transform * p, p_out, 'Shearing in yz direction failed')

    def test_shearing_zx(self):

        transform = shearing(zx=1)

        p = point(2,3,4)

        p_out = point(2,3,6)

        self.assertEqual( transform * p, p_out, 'Shearing in zx direction failed')

    def test_shearing_zy(self):

        transform = shearing(zy=1)

        p = point(2,3,4)

        p_out = point(2,3,7)

        self.assertEqual( transform * p, p_out, 'Shearing in zy direction failed')


    def test_chain_transform1(self):

        p = point(1,0,1)

        A = rotation_x(pi/2)
        B = scaling(5,5,5)
        C = translation(10,5,7)

        p2 = point(1,-1,0)

        self.assertEqual( A * p, p2, 'The rotation failed')

        p3 = point(5,-5,0)

        self.assertEqual( B * p2, p3, 'The chain scaling failed')

        p4 = point(15,0,7)

        self.assertEqual( C * p3, p4, 'The chain translation failed')


        self.assertEqual( C * B * A * p, p4, 'The chain transformations failed') 
