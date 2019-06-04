'''
Test for the object class
'''

import unittest
from raytrace.ray import ray
from raytrace.util import point, vector, identity_matrix
from raytrace.objects import sphere, intersect, intersection, intersections, hit
from raytrace.transformation import translation, scaling

class testObject(unittest.TestCase):

    def test_sphere(self):

        r = ray(point(0,0,-5), vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections')
        self.assertEqual( xs[0].t, 4.0, 't=4 should intersect')
        self.assertEqual( xs[1].t, 6.0, 't=6 should intersect')


    def test_sphere_1_intersect(self):

        r = ray(point(0,1,-5), vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections (virtual)')
        self.assertEqual( xs[0].t, 5.0, 't=5 should be an intersection time')
        self.assertEqual( xs[1].t, 5.0, 't=5 should be an intersection time')


    def test_sphere_miss(self):

        r = ray(point(0,2,-5), vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 0, 'There should be no intersections ')


    def test_sphere_inner(self):

        r = ray(point(0,0,0), vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections (virtual)')
        self.assertEqual( xs[0].t, -1.0, 't=-1 should be an intersection time')
        self.assertEqual( xs[1].t, 1.0, 't=1 should be an intersection time')


    def test_sphere_behind(self):

        r = ray(point(0,0,5), vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections (virtual)')
        self.assertEqual( xs[0].t, -6.0, 't=-6 should be an intersection time')
        self.assertEqual( xs[1].t, -4.0, 't=-4 should be an intersection time')


    def test_sphere_intersection(self):

        s = sphere()

        i = intersection(3.5,s)

        self.assertEqual( i.t, 3.5, 'Intersection time failed')
        self.assertEqual( i.object, s, 'Intersection object failed')


    def test_sphere_intersections(self):

        s = sphere()

        i1 = intersection(1,s)
        i2 = intersection(2,s)

        xs = intersections(i1,i2)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections')
        self.assertEqual( xs[0].t, 1, 'The first intersection time should be 1')
        self.assertEqual( xs[1].t, 2, 'The second intersection time should be 2')

    def test_sphere_intersect_group(self):

        r = ray(point(0,0,-5),vector(0,0,1))

        s = sphere()

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should be 2 intersections')
        self.assertEqual( xs[0].object, s, 'The intersection object failed')
        self.assertEqual( xs[1].object, s, 'The intersection object failed')


    def test_hit(self):

        s = sphere()

        i1 = intersection(1,s)
        i2 = intersection(2,s)

        xs = intersections(i1, i2)

        i = hit(xs)

        self.assertEqual(i, i1, 'The first hit is wrong')


    def teste_hit2(self):

        s = sphere()

        i1 = intersection(-1,s)
        i2 = intersection(1,s)

        xs = intersections(i1, i2)

        i = hit(xs)

        self.assertEqual(i, i2, 'The first hit is wrong')


    def teste_hit3(self):

        s = sphere()

        i1 = intersection(-1,s)
        i2 = intersection(-2,s)

        xs = intersections(i1, i2)

        i = hit(xs)

        self.assertIsNone(i, 'There should be no hit')


    def teste_hit4(self):

        s = sphere()

        i1 = intersection(5,s)
        i2 = intersection(7,s)
        i3 = intersection(-3,s)
        i4 = intersection(2,s)

        xs = intersections(i1, i2, i3, i4)

        i = hit(xs)

        self.assertEqual(i, i4, 'The first hit is wrong')


    def test_sphere_transform(self):

        s = sphere()
        
        self.assertEqual( s.transform, identity_matrix, 'The default sphere transformation should be the identity matrix')

        t = translation(2,3,4)
        s.set_transform(t)

        self.assertEqual( s.transform, t, 'The transformation shoud be translation')


    def test_sphere_transformed(self):

        r = ray(point(0,0,-5), vector(0,0,1))

        s = sphere()

        s.set_transform( scaling(2,2,2))

        xs = intersect(s,r)

        self.assertEqual( len(xs), 2, 'There should have been 2 intersections')
        self.assertEqual( xs[0].t, 3, 't=3 should have been present')
        self.assertEqual( xs[1].t, 7, 't=4 should have been present')


    def test_sphere_transformed2(self):

        r = ray(point(0,0,-5), vector(0,0,1))

        s = sphere()

        s.set_transform( translation(5,0,0))
        xs = intersect(s, r)

        self.assertEqual( len(xs) , 0, 'There sould be no intersection')
