'''
This is a python test for  color library
for Ray Tracing written by Arthur Scardua
'''

import unittest
from raytrace.util import color

class testColor(unittest.TestCase):
    ' test color class'

    def test_color(self):

        c = color(-0.5,0.4,1.7)

        equal = (c.red == -0.5) and (c.green == 0.4) and (c.blue == 1.7)
        self.assertTrue(equal,'The definition in color class should match')
    
    def test_color_add(self):

        c1 = color(1,0,0.5)
        c2 = color(0.6,0.4,0.25)
        c12 = color(1.6,0.4,0.75)

        self.assertEqual(c1+c2,c12,'The sum of colors should be equal')

    def test_color_sub(self):

        c1 = color(1,0,0.5)
        c2 = color(0.6,0.4,0.25)
        c12 = color(0.4,-0.4,0.25)

        self.assertEqual(c1-c2,c12,'The subtraction of colors should be equal')
    
    def test_color_scalar_mul(self):

        c1 = color(1,0,0.5)
        c2 = color(2,0,1)
        scalar = 2

        self.assertEqual(scalar * c1,c2,'The multiplication of colors and scalar should be equal')

    def test_color_mul(self):

        c1 = color(1,0,0.5)
        c2 = color(0.6,0.4,0.25)
        c12 = color(0.6,0,0.125)

        self.assertEqual(c1*c2,c12,'The multiplication of colors should be equal')   