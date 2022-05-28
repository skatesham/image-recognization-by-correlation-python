import unittest

import numpy

from src.correlation_processor import CorrelationProcessor


class CorrelationProcessorTestCase(unittest.TestCase):

    def setUp(self):
        self.input_pixel_image = CorrelationProcessor()
        self.pixels = numpy.arange(1, 10).tolist()

    def test_input(self):
        self.input_pixel_image.withPixels(self.pixels)
        pixels = self.input_pixel_image.getPixels()
        self.assertEqual(self.pixels, pixels)

    def test_input_image(self):
        self.input_pixel_image.withImageFlat("blank.png")
        pixels = self.input_pixel_image.getPixels()
        expected = [255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255]
        self.assertEqual(expected, pixels)

    def test_correlation(self):
        self.input_pixel_image.withPixels(self.pixels)
        self.input_pixel_image.correlatePattern(self.pixels)
        self.assertEqual([[1., 1.], [1., 1.]], self.input_pixel_image.getCorrelation())
        self.assertEqual(1, self.input_pixel_image.getCorrelationResult())

    def test_image_correlation(self):
        self.input_pixel_image.withImageFlat("chess.png")
        self.input_pixel_image.correlateFlatImagePattern("chess-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.input_pixel_image.getCorrelation())
        self.assertEqual(-1.0, self.input_pixel_image.getCorrelationResult())

    def test_image_correlation_half(self):
        self.input_pixel_image.withImageFlat("blank.png")
        self.input_pixel_image.correlateFlatImagePattern("half.png")
        none_correlation = [[float('NAN'), float('NAN')], [float('NAN'), 1.0]]
        numpy.testing.assert_equal(none_correlation, self.input_pixel_image.getCorrelation())
        numpy.testing.assert_equal(float('NAN'), self.input_pixel_image.getCorrelationResult())

    def test_inline_image_correlation(self):
        self.input_pixel_image.withImageFlat("chess-inline.png")
        self.input_pixel_image.correlateFlatImagePattern("chess-inline-inverse.png")
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.input_pixel_image.getCorrelation())
        self.assertEqual(-1.0, self.input_pixel_image.getCorrelationResult())

    def test_correlation_inverse(self):
        pixels = [
            9, 8, 7,
            6, 5, 4,
            3, 2, 1
        ]
        self.input_pixel_image.withPixels(self.pixels)
        self.input_pixel_image.correlatePattern(pixels)
        self.assertEqual([[1.0, -1.0], [-1.0, 1.0]], self.input_pixel_image.getCorrelation())
        self.assertEqual(-1, self.input_pixel_image.getCorrelationResult())

    def test_correlation_other(self):
        pixels = numpy.arange(10, 20).tolist()
        self.input_pixel_image.withPixels(pixels)
        different_input = numpy.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48]).tolist()
        self.input_pixel_image.correlatePattern(different_input)
        correlation = self.input_pixel_image.getCorrelation()
        self.assertEqual([[0.9999999999999999, 0.7586402890911867], [0.7586402890911869, 1.0]], correlation)
        self.assertEqual(0.76, self.input_pixel_image.getCorrelationResult())

    def test_correlation_error(self):
        pixels = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0
        ]
        error_input = [
            1, 1, 1,
            1, 1, 1,
            1, 1, 1
        ]
        self.input_pixel_image.withPixels(pixels)
        self.input_pixel_image.correlatePattern(error_input)
        none_correlation = [[float('NAN'), float('NAN')], [float('NAN'), float('NAN')]]
        numpy.testing.assert_equal(none_correlation, self.input_pixel_image.getCorrelation())
        numpy.testing.assert_equal(float('NAN'), self.input_pixel_image.getCorrelationResult())

    def test_correlation_result(self):
        self.input_pixel_image.withPixels(self.pixels)
        self.input_pixel_image.correlatePattern(self.pixels)
        self.assertEqual(1, self.input_pixel_image.getCorrelationResult())


if __name__ == '__main__':
    unittest.main()
