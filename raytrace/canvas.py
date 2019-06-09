'''
This is a python canvas library for Ray Tracing written by Arthur Scardua.
'''

from raytrace.util import color


class canvas():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._grid = [color(0, 0, 0)] * width * height

    def set_one_color(self, color_obj):
        self._grid = [color_obj] * self.width * self.height

    def __eq__(self, other):
        if isinstance(other, canvas):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __iter__(self):
        return self._grid.__iter__()

    def __setitem__(self, loc, data):
        x, y = loc
        if x >= self.width or y >= self.height:
            raise IndexError
        pos = x + self.width * y
        self._grid[pos] = data

    def __getitem__(self, loc):
        x, y = loc
        if x >= self.width or y >= self.height:
            raise IndexError
        pos = x + self.width * y
        return self._grid[pos]

    @staticmethod
    def to_color_range(number):
        if number < 0:
            return 0
        elif number > 1:
            return 255
        else:
            return round(number*255)

    def to_PPM(self):
        header = f'P3\n{self.width} {self.height}\n255\n'
        body = ''
        for num, color_obj in enumerate(self):
            red = self.to_color_range(color_obj.red)
            green = self.to_color_range(color_obj.green)
            blue = self.to_color_range(color_obj.blue)
            body += f'{red} {green} {blue}'
            if ((num+1) % self.width == 0) and num < self.width * (self.height-1):
                body += '\n'
            elif num != self.width * self.height - 1:
                body += ' '
        body+='\n'
        return self.crop_ppm(header + body)

    @staticmethod
    def crop_ppm(input_str):
        value = list(input_str)
        crop_len = 70
        counter = 0
        break_counter = 0
        break_n = False
        while counter < len(value):
            if value[counter] == '\n':
                break_counter = -1
            if break_counter == crop_len-1:
                break_n = True
                break_counter -= 1
            if break_n:
                if value[counter] == ' ':
                    value[counter] = '\n'
                    break_n = False
                    break_counter = -1
                else:
                    counter -= 2
            counter += 1
            break_counter += 1
        return ''.join(value)
