'''
Test for the ray class
'''

import unittest
from raytrace.util import point, vector
from raytrace.ray import ray, position, transform
from raytrace.transformation import translation, scaling

class testRay(unittest.TestCase):

    def test_ray(self):

        origin = point(1,2,3)

        direction = vector(4,5,6)

        r = ray(origin,direction)

        self.assertEqual( r.origin, origin, 'The origin of ray failed')
        self.assertEqual( r.direction, direction, 'The direction of ray failed')

    
    def test_position(self):

        r = ray(point(2,3,4), vector(1,0,0))

        self.assertEqual( position(r,0), point(2,3,4), 'Ray position failed')
        self.assertEqual( position(r,1), point(3,3,4), 'Ray position failed')
        self.assertEqual( position(r,-1), point(1,3,4), 'Ray position failed')
        self.assertEqual( position(r,2.5), point(4.5,3,4), 'Ray position failed')

    def test_transformation(self):

        r = ray(point(1,2,3), vector(0,1,0))

        m = translation(3,4,5)

        r2 = transform(r,m)

        self.assertEqual( r2.origin, point(4,6,8), 'The ray translation failed')
        self.assertEqual( r2.direction, vector(0,1,0), 'The ray translation failed')

        m2 = scaling(2,3,4)

        r3 = transform(r,m2)

        self.assertEqual( r3.origin, point(2,6,12), 'The ray scaling failed')
        self.assertEqual( r3.direction, vector(0,3,0), 'The ray scaling failed')
