import unittest

import numpy

from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_module import RecognizerModule


class CorrelationProcessorTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer_module = RecognizerModule()
        self.pixels = numpy.arange(1, 10).tolist()
        self.reader = PixelReader()

    def test_input_image(self):
        filename = "img/blank.png"
        pixels, width, height = self.reader.read_with_size(filename)
        self.recognizer_module.withPixels(pixels, width, height)
        pixels = self.recognizer_module.getPixels()
        expected = [255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255]
        self.assertEqual(expected, pixels)

    def test_image_correlation_half(self):
        filename = "img/blank.png"
        pixels, width, height = self.reader.read_with_size(filename)
        self.recognizer_module.withPixels(pixels, width, height)
        self.recognizer_module.recognize("img/half.png")
        none_correlation = [[float('NAN'), float('NAN')], [float('NAN'), 1.0]]
        numpy.testing.assert_equal(none_correlation, self.recognizer_module.getCorrelation())
        numpy.testing.assert_equal(float('NAN'), self.recognizer_module.getCorrelationResult())

    def test_image_inverted_correlation(self):
        filename = "img/chess.png"
        pixels, width, height = self.reader.read_with_size(filename)
        self.recognizer_module.withPixels(pixels, width, height)
        self.recognizer_module.recognize("img/chess-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.recognizer_module.getCorrelation())
        self.assertEqual(-1.0, self.recognizer_module.getCorrelationResult())

    def test_inversion_inline_image_correlation(self):
        filename = "img/chess-inline.png"
        pixels, width, height = self.reader.read_with_size(filename)
        self.recognizer_module.withPixels(pixels, width, height)
        self.recognizer_module.recognize("img/chess-inline-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.recognizer_module.getCorrelation())
        self.assertEqual(-1.0, self.recognizer_module.getCorrelationResult())


if __name__ == '__main__':
    unittest.main()
