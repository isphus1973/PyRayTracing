"""
The point light source library
"""
from raytrace.util import color

class PointLight:
    """
    Point light class.
    """

    def __init__(self, position, intensity):
        """
        Light source class.

        PointLight(position, intensity)

        A light source located at position and with intensity intensity.

        Parametes
        ---------
        -position (point): position where the light source is located.
        -intensity (color): intensity that the light source is.

        Return
        ------
        -PointLight: a PointLight object.
        """

        self.position = position
        self.intensity = intensity

class Material:
    """
    Scene object material class.
    """

    def __init__(self):
        """
        Material class.

        Material()

        Material class for scene objects.

        Parameters
        ----------

        Return
        ------
        -Material: the material class object.
        """

        self.color = color(1, 1, 1)
        self.ambient = 0.1
        self.diffusse = 0.9
        self.specular = 0.9
        self.shininess = 200.0

    def __eq__(self, other):
        """Material class equality"""

        if not isinstance(other, Material):
            return False

        equality = (self.ambient == other.ambient) and\
                (self.color == other.color) and\
                (self.diffusse == other.diffusse) and\
                (self.specular == other.specular) and\
                (self.shininess == other.shininess)
        return equality
