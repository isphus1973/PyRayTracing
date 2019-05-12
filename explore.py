from raytrace.canvas import *
from raytrace.util import *

c = canvas(10,2)
c1 = color(1,0.8,0.6)
c.set_one_color(c1)

ppm = c.to_PPM()

ppm_last_4_lines = '\n'.join(ppm.splitlines()[3:])

expected = ('255 204 153 '*5 + '255 204\n' + '153 255 204 '*4 + '153\n') * 2
