import unittest

from src.recognizer import Recognizer


class RecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = Recognizer()

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        answer = self.recognizer.recognize_patterns_v1(filename)
        self.assertEqual("987654321", answer)


if __name__ == '__main__':
    unittest.main()
