import unittest

import numpy

from src.domain.recognizer_module import RecognizerModule


class CorrelationProcessorTestCase(unittest.TestCase):

    def setUp(self):
        self.input_pixel_image = RecognizerModule()
        self.pixels = numpy.arange(1, 10).tolist()

    def test_input_image(self):
        self.input_pixel_image.withImageFlat("img/blank.png")
        pixels = self.input_pixel_image.getPixels()
        expected = [255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255]
        self.assertEqual(expected, pixels)

    def test_image_correlation_half(self):
        self.input_pixel_image.withImageFlat("img/blank.png")
        self.input_pixel_image.correlateFlatImagePattern("img/half.png")
        none_correlation = [[float('NAN'), float('NAN')], [float('NAN'), 1.0]]
        numpy.testing.assert_equal(none_correlation, self.input_pixel_image.getCorrelation())
        numpy.testing.assert_equal(float('NAN'), self.input_pixel_image.getCorrelationResult())

    def test_image_inverted_correlation(self):
        self.input_pixel_image.withImageFlat("img/chess.png")
        self.input_pixel_image.correlateFlatImagePattern("img/chess-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.input_pixel_image.getCorrelation())
        self.assertEqual(-1.0, self.input_pixel_image.getCorrelationResult())

    def test_inversion_inline_image_correlation(self):
        self.input_pixel_image.withImageFlat("img/chess-inline.png")
        self.input_pixel_image.correlateFlatImagePattern("img/chess-inline-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.input_pixel_image.getCorrelation())
        self.assertEqual(-1.0, self.input_pixel_image.getCorrelationResult())


if __name__ == '__main__':
    unittest.main()
