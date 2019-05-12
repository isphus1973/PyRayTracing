'''
This file computes a tracjectory and save a ppm file with it
'''

from raytrace.util import color, vector, point, rtTuple, normalize
from raytrace.canvas import canvas
from collections import namedtuple
import numpy as np

enviroment = namedtuple('Enviroment', 'gravity wind')

class trajectory:
    def __init__(self,vel,pos,env,dt):
        if not (vel.is_vector() and pos.is_point() and isinstance(env,enviroment)):
            print(vel.is_vector() and pos.is_point() and isinstance(env,enviroment))
            raise TypeError
        self.vel = vel
        self.dt = dt
        self.pos = pos
        self.env = env
        self.tracjectory = self.make_trajectory()

    def make_trajectory(self):
        wind = self.env.wind
        gravity = self.env.gravity

        traj = list()
        pos = self.pos
        vel = self.vel 

        while pos.y >= 0:
            traj.append((pos.x,pos.y))
            pos+= vel * self.dt
            vel+= gravity * self.dt + wind * self.dt
        
        return traj

    def canvas(self):
        canvas_list = {(round(x),round(y)) for x,y in self.tracjectory}

        max_x = max(canvas_list, key=lambda loc: loc[0])[0]+1
        max_y = max(canvas_list, key=lambda loc: loc[1])[1]+1

        c = canvas(max_x,max_y)
        background_c = color(0.9,0.9,0.9)
        c.set_one_color(background_c)

        for pt in canvas_list:
            x = pt[0]
            y = max_y-pt[1]-1
            pt2 = x,y
            c[pt2] = color(1,0,0)

        return c

p0 = point(0,0,0)
v0 = normalize(vector(1,4,0)) * 20

env = enviroment(vector(0,-1,0),vector(0.5,0,0))

tt = trajectory(v0,p0,env,0.001)

c = tt.canvas()

ppm = c.to_PPM()

with open('image.ppm','w') as f:
    f.write(ppm)

np_trajectory = np.array(tt.tracjectory)

import matplotlib.pyplot as plt

plt.plot(np_trajectory[:,0],np_trajectory[:,1])

plt.show()