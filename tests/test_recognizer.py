import unittest

from src.recognizer_application import RecognizerApplication


class RecognizerTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = RecognizerApplication()

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        result, patterns = self.recognizer.recognize(filename)
        self.assertEqual("987654321", result)


if __name__ == '__main__':
    unittest.main()
