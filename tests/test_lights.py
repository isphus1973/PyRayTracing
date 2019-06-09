'''
Test for the ray class
'''

import unittest
from raytrace.objects import sphere
from raytrace.light import PointLight, Material
from raytrace.util import color, point

class TestLight(unittest.TestCase):
    """Test of light sources"""

    def test_pointlight(self):
        """
        Tests the creation of a light source.
        """

        intensity = color(1, 1, 1)
        position = point(0, 0, 0)

        light = PointLight(position, intensity)

        self.assertEqual(light.position, position, "Light position is wrong.")
        self.assertEqual(light.intensity, intensity, "Light intensity is wrong")

    def test_material(self):
        """Tests the material class constructor"""

        m_var = Material()

        self.assertEqual(m_var.color, color(1, 1, 1),\
            'Material color failed')
        self.assertEqual(m_var.ambient, 0.1,\
            'Material ambient failed')
        self.assertEqual(m_var.diffusse, 0.9,\
            'Material diffuse failed')
        self.assertEqual(m_var.specular, 0.9,\
            'Material specular failed')
        self.assertEqual(m_var.shininess, 200.0,\
            'Material shininess failed')

    def test_sphere_material(self):
        """Tests the sphere material."""

        s_var = sphere()
        m_var = s_var.material

        self.assertEqual(m_var, Material(),\
                'The m_var should be a material')

        m_var = Material()
        m_var.ambient = 1
        s_var.material = m_var

        self.assertEqual(s_var.material, m_var,\
                'The sphere material failed.')
