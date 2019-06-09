'''
This create the objects classes
'''

from math import sqrt
from raytrace.util import dot, point, identity_matrix, inverse
from raytrace.transformation import scaling, translation
from raytrace.ray import transform
from raytrace.light import Material

class intersection:
    '''
    Intersection between a ray and a object.

    intersection(t,obj)

    Intersection between an ray and a object obj in the time t.
    
    Parameters
    ----------

    -t (float): time intersection.
    -obj (scene_obj): object intersected.

    Return
    ------

    -intersection: intersection object
    '''

    def __init__(self, t, obj):
        self.t = t
        self.object = obj


class intersections:
    '''
    Group of intersections

    intersections(*args)

    Group os intersections in *args.

    Parameters
    ----------

    -*args (intersection): intersections

    Return
    ------

    -intersections: intersections object
    '''

    def __init__(self,*args):
        if len(args) == 0:
            self.intersections = []
        else:
            self.intersections = sorted(args, key=lambda loc: loc.t)

    def __getitem__(self,pos):
        return self.intersections[pos]

    def __len__(self):
        return len(self.intersections)

def intersect(obj, r):
    '''
    Intercection time between obj and r.

    intersect(obj, r)

    Intersection beween an object obj and a ray r that returns the intersection objects the ray
    intersects the obj. If there is no intersection, return an empty array.

    Parameters
    ----------

    -obj (scene_obj): object in the scene to intersect
    -r (ray): ray to intersect

    Return
    ------
    -intersections: list with all intersections . Tangent intersections appear twice.
    '''
    
    if not isinstance(obj, scene_obj):
        raise TypeError('obj should be an scene_obj')

    rnew = transform(r, inverse(obj.transform))

    if isinstance(obj, sphere):

        d = rnew.direction
        r0 = rnew.origin
        rc = obj.center
        
        r2 = obj.r * obj.r
        D = r0 - rc

        D2 = dot(D,D)
        Dd = dot(D,d)
        d2 = dot(d,d)

        discriminant =  Dd * Dd - d2 * (D2 - r2)

        if discriminant < 0:
            return intersections()

        t1 = ( - Dd - sqrt(discriminant)) / d2
        t2 = ( - Dd + sqrt(discriminant)) / d2

        i1 = intersection(t1, obj)
        i2 = intersection(t2, obj)

        return intersections( i1, i2 )
    else:
        raise NotImplementedError('Not implemented')

def hit(xs):
    '''
    Return the first ray hit.

    hit(xs)

    The first ray hit given the intersections xs.

    Parameters
    ----------

    -xs (intersections): ray intersections

    Return
    ------

    -intersection: return the intersection with the smallest positve time
    '''
    
    positive_intersections = [inter for inter in xs.intersections if inter.t >=0 ]

    if len(positive_intersections) == 0:
        return None

    return min(positive_intersections, key=lambda loc: loc.t)

class scene_obj:
    '''
    Scene object,

    scene_obj()

    The basic scene object.
    
    Parameters
    ----------

    Return
    ------

    -scene_obj: scene object.
    '''

    def __init__(self):
        self.transform = identity_matrix

    def set_transform(self, m):
        '''
        Set a new transformation for the object.

        obj.set_transform(m)

        Update the transformation of the objecto to m.

        Parameters
        ----------

        -m (matrix): a matrix that represents a transformation.

        Return
        ------

        -True
        '''
       
        self.transform = m

        return True

class sphere(scene_obj):
    '''
    Sphere class

    sphere(center,r=1)

    Create a sphere um the position center with radii r

    Parameters
    ---------

    -center (point): point of the center
    -r (float): radii

    Return
    ------

    -sphere: scene object sphere
    '''

    def __init__(self,center=point(0,0,0),r=1):
        self.center = center
        self.r = r
        self.transform = scaling(r,r,r) * translation(*center) 
        self.material = Material()
