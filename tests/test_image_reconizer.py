import unittest

from src.image_reader import ImageReader
from src.image_reconizer import ImageRecognizer


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = ImageRecognizer()
        self.reader = ImageReader()

    def test_process_sample_search_8(self):
        number = "8"
        filename = f'../resources/img/numbers/{number}.png'
        sample = self.reader.read_flat(filename)
        result = self.recognizer.process_sample(sample)
        self.assertEqual(number, result)

    def test_process_image_search_numbers(self):
        filename = f'../resources/img/numbers/{ "all_numbers" }.png'
        result = self.recognizer.process_image(filename)
        self.assertEqual("987654321", result)


if __name__ == '__main__':
    unittest.main()
