import unittest

from src.domain.recognizer_service import RecognizerProcessor


class NumberRecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = RecognizerProcessor()

    def test_process_sample_search_8(self):
        number = "8"
        result = self.recognizer.process_image(f'../resources/img/numbers/{number}.png').getAnswer()
        self.assertEqual(number, result)

    def test_process_image_search_numbers(self):
        filename = '../img/all_numbers.png'
        result = self.recognizer.process_image(filename).getAnswer()
        self.assertEqual("987654321", result)
        expected_best_results = {
            0: [],
            1: [1.0],
            2: [0.98],
            3: [0.89],
            4: [0.97],
            5: [1.0],
            6: [0.97],
            7: [0.91],
            8: [0.97],
            9: [1.0]
        }
        self.assertEqual(expected_best_results, self.recognizer.getBestResult())
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
        self.assertEqual(expected_best_results, self.recognizer.getFilteredResults())


if __name__ == '__main__':
    unittest.main()
