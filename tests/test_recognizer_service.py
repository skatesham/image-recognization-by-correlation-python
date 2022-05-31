import unittest

from src.domain.pattern import Pattern
from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_service import RecognizerService


class NumberRecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = RecognizerService()
        self.reader = PixelReader()

    def test_process_sample_search_8(self):
        number_pattern = "8"
        filename = f'../resources/img/numbers/{number_pattern}.png'
        matriz, width, height = self.reader.read_as_matriz(filename)
        patterns = self.build_patterns()
        target_image = Pattern(filename, matriz, height, width)
        process_result = self.recognizer.process_image(target_image, patterns)
        self.assertEqual(number_pattern, process_result[0])

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        matriz, width, height = self.reader.read_as_matriz(filename)
        patterns = self.build_patterns()
        target_image = Pattern(filename, matriz, height, width)
        result, __ = self.recognizer.process_image(target_image, patterns)
        self.assertEqual("987654321", result)
        expected_best_results = {
            0: '',
            1: 1.0,
            2: 0.98,
            3: 0.89,
            4: 0.97,
            5: 1.0,
            6: 0.97,
            7: 0.91,
            8: 0.97,
            9: 1.0
        }
        self.assertEqual(expected_best_results, dict((x.name, x.get_best_result()) for x in patterns))
        expected_best_results = {
            0: [0.68, 0.7, 0.77, 0.83, 0.85],
            1: [0.34, 0.38, 0.4, 0.55, 1.0],
            2: [0.62, 0.64, 0.72, 0.83, 0.98],
            3: [0.72, 0.74, 0.76, 0.84, 0.89],
            4: [0.44, 0.45, 0.52, 0.67, 0.97],
            5: [0.66, 0.73, 0.73, 0.88, 1.0],
            6: [0.76, 0.77, 0.84, 0.86, 0.97],
            7: [0.41, 0.48, 0.52, 0.62, 0.91],
            8: [0.74, 0.78, 0.78, 0.87, 0.97],
            9: [0.73, 0.73, 0.76, 0.77, 1.0]
        }
        self.assertEqual(expected_best_results, dict((x.name,x.get_filtered_results()) for x in patterns))

    def build_patterns(self, patterns_filename="../resources/img/numbers/{}.png"):
        patterns = list()
        for name in range(10):
            pixels, width, height = self.reader.read_as_list(patterns_filename.format(name))
            pattern = Pattern(name, pixels, height, width)
            patterns.append(pattern)
        return patterns


if __name__ == '__main__':
    unittest.main()
