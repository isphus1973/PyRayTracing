'''
This is the ray class
'''

class ray:
    '''
    Ray class used for ray propagation.

    ray(origin, direction)

    Ray class for 3D ray propagation.

    Parameters
    ----------

    -origin (point): origin point of the ray.
    -direction (vector): direction of the ray propagation.

    Return
    ------

    -ray: a ray object.
    '''

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction


def position(ray,t):
    return ray.origin + ray.direction * t

def transform(r, m):
    '''
    Transform a ray.

    transform(r, m)

    Transform a ray usint the transformarion m.

    Parameters
    ----------

    -r (ray): ray.
    -m (matrix): transformation matrix

    Return
    ------

    -ray: transformed ray
    '''

    return ray( m * r.origin, m * r.direction )
