'''
This file draws the shadow of the sphere in the canvas
'''

from raytrace.util import color, point, vector
from raytrace.ray import ray
from raytrace.canvas import canvas
from raytrace.objects import sphere, intersect, hit
from raytrace.transformation import translation, scaling

CANVAS_DISTANCE = 100
CANVAS_H = 1000
CANVAS_W = 1000
HIT_COLOR = color(1,0,0)

c = canvas(CANVAS_H, CANVAS_W)

background_c = color(0.9,0.9,0.9)
c.set_one_color(background_c)

with open('shadow_sphere.ppm','w') as f:
    f.write(c.to_PPM())

print('blank canvas wrote')

pad_x = - CANVAS_W /2
pad_y = - CANVAS_H /2

s = sphere()
trans = scaling(200,200,1) * translation(0, 0, 800)
s.set_transform(trans)

print('{:04d},{:04d}'.format(0,0), end='\r')
h = False
for i in range(CANVAS_W):
    #print()
    for j in range(CANVAS_H):
        print('{:04d},{:04d}'.format(i,j),end='\r') 
        r = ray(point(0,0,0), vector(i + pad_x, -pad_y - j, CANVAS_DISTANCE))
        inter = intersect(s, r)
        if hit(inter) != None:
            c[i,j] = HIT_COLOR
            h = True
        #if h:
            #print('\033[48;2;255;0;0m  \033[0m', end='', flush=True)
        #else:
            #print('\033[48;2;230;230;230m  \033[0m', end='', flush=True)
        h = False

PPM = c.to_PPM()

with open('shadow_sphere.ppm','w') as f:
    f.write(PPM)


