"""
The point light source library
"""
from raytrace.util import color, normalize, dot, reflect

BLACK = color(0, 0, 0)

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

def lighting(material, light, point, eyev, normalv):
    """
    Create the lighting of and ray.

    lighting(material, light, point, eyev, normalv)

    Creates the lighting of the ray.

    Parameters
    ----------
    -material (Material): the material of the object.
    -light (PointLight): source of light.
    -point (point): point to be iluminated.
    -eyev (vector): eye vector direction.
    -normalv (vector): normal vector of the object.

    Result
    ------
    -color: the output color.
    """

    effective_color = material.color * light.intensity

    lightv = normalize(light.position - point)

    ambient = effective_color * material.ambient

    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:

        diffusse = BLACK
        specular = BLACK

    else:
        diffusse = effective_color * material.diffusse *\
                light_dot_normal

        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = BLACK
        else:
            factor = pow(reflect_dot_eye, material.shininess)
            specular = light.intensity * material.specular\
                    * factor
    return ambient + diffusse + specular
