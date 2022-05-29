import numpy
from pip._internal.utils.deprecation import deprecated

from src.domain.pixel_reader import PixelReader


class RecognizerModule:

    def __init__(self) -> None:
        super().__init__()
        self.reader = PixelReader()
        self.pixels = []
        self.correlation = []
        self.input_pattern = []
        self.pattern_width = -1
        self.pattern_height = -1

    def withPixels(self, pixels, width=0, height=0):
        self.pixels = pixels
        self.pattern_width = width
        self.pattern_height = height
        return self

    def correlatePattern(self, pixels):
        self.input_pattern = pixels
        self.correlation = numpy.corrcoef(self.pixels, pixels).tolist()
        return self

    def recognize(self, filename):
        flat_image, width, height = self.reader.read_with_size(filename)
        self.correlatePattern(flat_image)
        return self

    def getPixels(self):
        return self.pixels

    def getCorrelation(self):
        return self.correlation

    def getCorrelationResult(self):
        correlation_x_with_y = self.correlation[0][1]
        return float("{:.2f}".format(correlation_x_with_y))

