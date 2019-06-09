'''
Test for the ray class
'''

from math import sqrt, pi
import unittest
from raytrace.objects import sphere
from raytrace.util import point, normalize, normal_at, vector, reflect
from raytrace.transformation import translation, scaling, rotation_z

class TestNormal(unittest.TestCase):
    """Test of normal vectors"""

    def test_sphere_x(self):
        """Test sphere normal in x direction"""

        s_var = sphere()
        n_var = normal_at(s_var, point(1, 0, 0))

        self.assertEqual(n_var, vector(1, 0, 0), "Sphere normal in x direction failed.")


    def test_sphere_y(self):
        """Test sphere normal in y direction"""

        s_var = sphere()
        n_var = normal_at(s_var, point(0, 1, 0))

        self.assertEqual(n_var, vector(0, 1, 0), "Sphere normal in y direction failed.")


    def test_sphere_z(self):
        """Test sphere normal in z direction"""

        s_var = sphere()
        n_var = normal_at(s_var, point(0, 0, 1))

        self.assertEqual(n_var, vector(0, 0, 1), "Sphere normal in z direction failed.")


    def test_sphere_nonaxial(self):
        """Test sphere normal in nonaxial direction"""

        s_var = sphere()
        n_var = normal_at(s_var, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))

        self.assertEqual(n_var, vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3),\
                "Sphere normal in z direction failed.")

    def test_sphere_normal_vector_is_normal(self):
        """Tests if the normal vector is normal in a sphere"""

        s_var = sphere()
        n_var = normal_at(s_var, point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))

        self.assertEqual(n_var, normalize(n_var), 'Normal in a sphere is not normalized.')

    def test_sphere_translated(self):
        """Tests a sphere normal vector under translation"""

        s_var = sphere()
        s_var.set_transform(translation(0, 1, 0))

        n_var = normal_at(s_var, point(0, 1.70711, -0.70711))

        self.assertEqual(n_var, vector(0, 0.70711, -0.70711),\
                'The normal in the translated sphere is wrong.')

    def test_sphere_transformed(self):
        "Tests the sphere normal vector under a transformation"

        s_var = sphere()
        m_var = scaling(1, 0.5, 1)*rotation_z(pi/5)
        s_var.set_transform(m_var)

        n_var = normal_at(s_var, point(0, sqrt(2)/2, -sqrt(2)/2))

        self.assertEqual(n_var, vector(0, 0.97014, -0.24254),\
                'The normal of an sphere transformed is wrong.')


    def test_reflection(self):
        """Refleting a vector approaching at 45d"""

        v_var = vector(1, -1, 0)
        n_var = vector(0, 1, 0)
        r_var = reflect(v_var, n_var)

        self.assertEqual(r_var, vector(1, 1, 0), 'The 45 reflection failed.')

    def test_reflection_slanted(self):
        """Tests a reflecting a vector off a slanted surface"""

        v_var = vector(0, -1, 0)
        n_var = vector(sqrt(2)/2, sqrt(2)/2, 0)
        r_var = reflect(v_var, n_var)

        self.assertEqual(r_var, vector(1, 0, 0), "The slanted reflection failed.")
