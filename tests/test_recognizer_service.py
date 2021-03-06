import unittest

from src.domain.model.pattern import Pattern
from src.domain.utils.pixel_reader import PixelReaderUtils
from src.recognizer_service import RecognizerService


class NumberRecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = RecognizerService()

    def test_process_sample_search_8(self):
        number_pattern = "8"
        filename = f'../resources/img/numbers/{number_pattern}.png'
        matriz, width, height = PixelReaderUtils.read_as_matriz(filename)
        patterns = self.build_patterns()
        target_image = Pattern(filename, matriz, height, width)
        process_result = self.recognizer.process_image_without_acquisition(target_image, patterns)
        self.assertEqual(number_pattern, process_result[0])

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        matriz, width, height = PixelReaderUtils.read_as_matriz(filename)
        patterns = self.build_patterns()
        target_image = Pattern(filename, matriz, height, width)
        result = self.recognizer.process_image_without_acquisition(target_image, patterns)
        self.assertEqual("987654321", result)

    def build_patterns(self, patterns_filename="../resources/img/numbers/{}.png"):
        patterns = list()
        for name in range(10):
            pixels, width, height = PixelReaderUtils.read_as_list(patterns_filename.format(name))
            pattern = Pattern(name, pixels, height, width)
            patterns.append(pattern)
        return patterns


if __name__ == '__main__':
    unittest.main()
