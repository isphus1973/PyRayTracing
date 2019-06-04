'''
This file draws a clock using the matrix transformations
'''

from raytrace.util import color, point
from raytrace.canvas import canvas
from raytrace.transformation import rotation_z
from math import pi

p = point(100,0,0)
div = 12

ticks = [2* n * pi/div for n in range(div) ]

points = [ rotation_z(tick) * p for tick in ticks ]

canvas_list = {(round(pos.x), round(pos.y)) for pos in points}

min_x = min(canvas_list,key=lambda loc: loc[0])[0]
pad_x = 0 if min_x >= 0 else - min_x

min_y = min(canvas_list, key= lambda loc: loc[1])[1]
pad_y = 0 if min_y >=0 else - min_y

max_x = max(canvas_list, key = lambda loc: loc[0])[0] + 1 + pad_x
max_y = max(canvas_list, key = lambda loc: loc[1])[1] +1 + pad_y

canvas_list_padded = [(x+pad_x,max_y -1-y-pad_y) for x,y in canvas_list]

c = canvas(max_x, max_y)

background_c = color(0.9,0.9,0.9)
c.set_one_color(background_c)

for pt in canvas_list_padded:
    c[pt] = color(1,0,0)

ppm = c.to_PPM()

with open('clock.ppm','w') as f:
    f.write(ppm)

