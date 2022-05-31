import unittest

from src.recognizer import Recognizer

import json

class RecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = Recognizer()

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        result_process = self.recognizer.recognize_patterns(filename)
        self.assertEqual("987654321", result_process.answer)


if __name__ == '__main__':
    unittest.main()
