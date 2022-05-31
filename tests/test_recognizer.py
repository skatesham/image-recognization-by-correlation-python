import unittest

from src.recognizer import Recognizer


class RecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = Recognizer()

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        result, patterns = self.recognizer.recognize_patterns(filename)
        self.assertEqual("987654321", result)
        best_results = [
            [0.68, 0.7, 0.77, 0.83, 0.85],
            [0.34, 0.38, 0.4, 0.55, 1.0],
            [0.62, 0.64, 0.72, 0.83, 0.98],
            [0.72, 0.74, 0.76, 0.84, 0.89],
            [0.44, 0.45, 0.52, 0.67, 0.97],
            [0.66, 0.73, 0.73, 0.88, 1.0],
            [0.76, 0.77, 0.84, 0.86, 0.97],
            [0.41, 0.48, 0.52, 0.62, 0.91],
            [0.74, 0.78, 0.78, 0.87, 0.97],
            [0.73, 0.73, 0.76, 0.77, 1.0]]
        self.assertEqual(best_results, [x.get_filtered_results() for x in patterns])


if __name__ == '__main__':
    unittest.main()
