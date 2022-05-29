import numpy

from src.domain.pixel_reader import PixelReader


class RecognizerModule:

    def __init__(self) -> None:
        super().__init__()
        self.image_reader = PixelReader()
        self.pixels = []
        self.correlation = []
        self.input_pattern = []
        self.pattern_width = -1
        self.pattern_height = -1

    def withImageFlat(self, filename):
        flat_image, width, height = self.image_reader.read_detailed(filename)
        self.pattern_width = width
        self.pattern_height = height
        self.pixels = flat_image

    def withPixels(self, pixels):
        self.pixels = pixels
        return self

    def correlatePattern(self, pixels):
        self.input_pattern = pixels
        self.correlation = numpy.corrcoef(self.pixels, pixels).tolist()
        return self

    def correlateFlatImagePattern(self, filename):
        flat_image, width, height = self.image_reader.read_detailed(filename)
        self.correlatePattern(flat_image)
        return self

    def getPixels(self):
        return self.pixels

    def getCorrelation(self):
        return self.correlation

    def getCorrelationResult(self):
        correlation_x_with_y = self.correlation[0][1]
        return float("{:.2f}".format(correlation_x_with_y))

