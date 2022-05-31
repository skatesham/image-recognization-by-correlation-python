import unittest

import numpy

from src.domain.pixel_reader_utils import PixelReader
from src.domain.recognizer_module import RecognizerModule


class RecognizerModuleTestCase(unittest.TestCase):

    def setUp(self):
        self.pixels = numpy.arange(1, 10).tolist()

    def test_image_correlation_half(self):
        pattern_pixels, __, __ = PixelReader.read_as_list("img/blank.png")
        target_pixels, __, __ = PixelReader.read_as_list("img/half.png")
        result = RecognizerModule.calculate_correlation(pattern_pixels, target_pixels)
        numpy.testing.assert_equal(float('NAN'), result)

    def test_image_inverted_correlation(self):
        pattern_pixels, __, __ = PixelReader.read_as_list("img/chess.png")
        target_pixels, __, __ = PixelReader.read_as_list("img/chess-inverse.png")
        result = RecognizerModule.calculate_correlation(pattern_pixels, target_pixels)
        numpy.testing.assert_equal(-1.0, result)

    def test_inversion_inline_image_correlation(self):
        pattern_pixels, __, __ = PixelReader.read_as_list("img/chess-inline.png")
        target_pixels, __, __ = PixelReader.read_as_list("img/chess-inline-inverse.png")
        result = RecognizerModule.calculate_correlation(pattern_pixels, target_pixels)
        numpy.testing.assert_equal(-1.0, result)


if __name__ == '__main__':
    unittest.main()
