import unittest

import numpy

from src.domain.recognizer_module import RecognizerModule


class RecognizerModuleCorrelationTestCase(unittest.TestCase):

    def setUp(self):
        self.pixels = numpy.arange(1, 10).tolist()

    def test_correlation(self):
        self.assertEqual(1, RecognizerModule.calculate_correlation(self.pixels, self.pixels))

    def test_correlation_inverse(self):
        pixels = [
            9, 8, 7,
            6, 5, 4,
            3, 2, 1
        ]
        result = RecognizerModule.calculate_correlation(self.pixels, pixels)
        self.assertEqual(-1, result)

    def test_correlation_classic_tested_problem(self):
        pixels = numpy.arange(10, 20).tolist()
        different_input = numpy.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48]).tolist()
        result = RecognizerModule.calculate_correlation(pixels, different_input)
        self.assertEqual(0.76, result)

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
        result = RecognizerModule.calculate_correlation(self.pixels, error_input)
        numpy.testing.assert_equal(float('NAN'), result)


if __name__ == '__main__':
    unittest.main()
