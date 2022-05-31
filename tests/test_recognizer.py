import unittest

from src.recognizer import Recognizer


class RecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = Recognizer()

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        result, patterns = self.recognizer.recognize_patterns(filename)
        self.assertEqual("987654321", result)


if __name__ == '__main__':
    unittest.main()
