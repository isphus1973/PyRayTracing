'''
This is the test for the canvas class
'''

import unittest
from raytrace.canvas import canvas
from raytrace.util import color


class testCanvas(unittest.TestCase):
    'Test for the canvas class'

    def test_canvas(self):

        c = canvas(10, 20)

        self.assertEqual(c.width, 10, 'The canvas width should be 10')
        self.assertEqual(c.height, 20, 'The canvas height should be 20')

        black_color = color(0, 0, 0)

        is_black = [c_color == black_color for c_color in c]

        self.assertTrue(all(is_black), 'All canvas pixels should be black')

    def test_set_pixel(self):

        c = canvas(10, 20)

        red = color(1, 0, 0)
        black = color(0, 0, 0)
        c[2, 3] = red

        self.assertEqual(c[2, 3], red, 'The pixel at (2,3) should be red')
        self.assertEqual(c[0, 0], black, 'The pixel at (2,3) should be red')
        self.assertEqual(c._grid[32], red, 'The pixel at (2,3) should be red')

        with self.assertRaises(IndexError):
            c[31, 21] = 10

    def test_canvas_to_PPM(self):

        c = canvas(5, 4)

        ppm = c.to_PPM()
        first_three_lines = ppm.splitlines()[:3]
        expected = ['P3', '5 4', '255']

        self.assertEqual(first_three_lines, expected,
                         'The frist lines of generated PPM is expected')

    def test_PPM_colors(self):

        c = canvas(5, 3)
        c1 = color(1.5, 0, 0)
        c2 = color(0, 0.5, 0)
        c3 = color(-0.5, 0, 1)

        c[0, 0] = c1
        c[2, 1] = c2
        c[4, 2] = c3
        ppm = c.to_PPM()

        ppm_last_3_lines = '\n'.join(ppm.splitlines()[-3:])
        expected = '255 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n' +\
            '0 0 0 0 0 0 0 128 0 0 0 0 0 0 0\n' +\
            '0 0 0 0 0 0 0 0 0 0 0 0 0 0 255'

        self.assertEqual(ppm_last_3_lines,expected,'The generated PPM is not what expected')

    def test_PPM_crop(self):

        c = canvas(10,2)
        c1 = color(1,0.8,0.6)
        c.set_one_color(c1)

        ppm = c.to_PPM()

        ppm_last_4_lines = '\n'.join(ppm.splitlines()[3:])+ppm[-1]

        expected = ('255 204 153 '*5 + '255 204\n' + '153 255 204 '*4 + '153\n') * 2
        
        self.assertEqual(ppm_last_4_lines,expected,\
            'The generated ppm has not the expected crop')
