import unittest

import numpy

from src.domain.pixel_reader_utils import PixelReader
from src.domain.correlation_utils import CorrelationUtils


def buildFileName(number):
    return f'../resources/img/numbers/{number}.png'


class ConfusionMatrizTestCase(unittest.TestCase):

    def test_all_numbers_correlation(self):
        results = []
        for y in range(10):
            result_x = []
            for x in range(10):
                result = ConfusionMatrizTestCase.correlate(y, x)
                result_x.append(result)
            results.append(result_x)
        # Debug on this variable for get confusion matriz
        numpy_array = numpy.array(results)
        self.assertEqual([[1.0, 0.14, 0.55, 0.69, 0.48, 0.7, 0.85, 0.28, 0.78, 0.85],
                          [0.14, 1.0, 0.33, 0.31, 0.32, 0.28, 0.19, 0.4, 0.22, 0.17],
                          [0.55, 0.33, 1.0, 0.73, 0.32, 0.5, 0.48, 0.61, 0.59, 0.64],
                          [0.69, 0.31, 0.73, 1.0, 0.39, 0.71, 0.69, 0.53, 0.85, 0.76],
                          [0.48, 0.32, 0.32, 0.39, 1.0, 0.35, 0.45, 0.28, 0.46, 0.36],
                          [0.7, 0.28, 0.5, 0.71, 0.35, 1.0, 0.84, 0.41, 0.78, 0.73],
                          [0.85, 0.19, 0.48, 0.69, 0.45, 0.84, 1.0, 0.28, 0.87, 0.77],
                          [0.28, 0.4, 0.61, 0.53, 0.28, 0.41, 0.28, 1.0, 0.4, 0.38],
                          [0.78, 0.22, 0.59, 0.85, 0.46, 0.78, 0.87, 0.4, 1.0, 0.78],
                          [0.85, 0.17, 0.64, 0.76, 0.36, 0.73, 0.77, 0.38, 0.78, 1.0]], results)

    @staticmethod
    def correlate(pattern_number, input_number):
        pattern_file_name = buildFileName(pattern_number)
        input_file_name = buildFileName(input_number)
        pattern_pixels, width, height = PixelReader.read_as_list(pattern_file_name)
        target_pixels, width, height = PixelReader.read_as_list(input_file_name)
        return CorrelationUtils.calculate_correlation(pattern_pixels, target_pixels)


if __name__ == '__main__':
    unittest.main()
