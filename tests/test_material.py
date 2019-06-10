"""
Tests the material and reflections
"""

from math import sqrt
import unittest
from raytrace.light import Material, PointLight, lighting
from raytrace.util import vector, color, point

class TestMaterial(unittest.TestCase):
    """Tests the material."""

    m_var = Material()
    position = point(0, 0, 0)

    def test_lightning1(self):
        """Lighting with the eye between the light and the surface."""

        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), color(1, 1, 1))

        result = lighting(self.m_var, light, self.position, eyev, normalv)

        self.assertEqual(result, color(1.9, 1.9, 1.9), \
                'The lighting function failed.')

    def test_lightning2(self):
        """Lighting with the eye 45 degrees from the suface-light line"""

        eyev = vector(0, sqrt(2)/2, sqrt(2)/2)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, -10), color(1, 1, 1))

        result = lighting(self.m_var, light, self.position, eyev, normalv)

        self.assertEqual(result, color(1.0, 1.0, 1.0), \
                'The lighting function failed.')

    def test_lightning3(self):
        """Lighting with the light 45 degrees from the suface-eye line"""

        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), color(1, 1, 1))

        result = lighting(self.m_var, light, self.position, eyev, normalv)

        self.assertEqual(result, color(0.7364, 0.7364, 0.7364), \
                'The lighting function failed.')

    def test_lightning4(self):
        """Lighting with the light and the eye 45 degrees from the suface line"""

        eyev = vector(0, -sqrt(2)/2, -sqrt(2)/2)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 10, -10), color(1, 1, 1))

        result = lighting(self.m_var, light, self.position, eyev, normalv)

        self.assertEqual(result, color(1.6364, 1.6364, 1.6364), \
                'The lighting function failed.')

    def test_lightning5(self):
        """Lighting with the light hidden behind the surfice"""

        eyev = vector(0, 0, -1)
        normalv = vector(0, 0, -1)
        light = PointLight(point(0, 0, 10), color(1, 1, 1))

        result = lighting(self.m_var, light, self.position, eyev, normalv)

        self.assertEqual(result, color(0.1, 0.1, 0.1), \
                'The lighting function failed.')
