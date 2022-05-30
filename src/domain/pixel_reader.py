import numpy
from PIL import Image


class PixelReader:

    def read(self, filename):
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

    def read_flat(self, filename):
        read, width, height = self.read(filename)
        return [item for lines in read for item in lines]

    def read_flat_with_size(self, filename):
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
