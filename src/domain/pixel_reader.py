import numpy
from PIL import Image


class PixelReader:

    def read_as_matriz(self, filename):
        img = Image.open(filename)
        width, height = img.size
        image_array = numpy.asarray(img)
        pixels = []
        for lines in image_array:
            line = []
            for item in lines:
                line.append(item[0])
            pixels.append(line)
        return pixels, width, height

    def read_as_list(self, filename):
        img = Image.open(filename)
        width, height = img.size
        image_array = numpy.asarray(img)
        pixels = []
        for lines in image_array:
            line = []
            for item in lines:
                line.append(item[0])
            pixels.append(line)
        return [item for lines in pixels for item in lines], width, height
