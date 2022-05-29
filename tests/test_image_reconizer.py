import unittest

from src.domain.img_reader import ImageReader
from src.domain.number_reconizer import NumberImageRecognizer


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.recognizer = NumberImageRecognizer()
        self.reader = ImageReader()

    def test_process_sample_search_8(self):
        number = "8"
        filename = f'../resources/img/numbers/{number}.png'
        sample = self.reader.read_flat(filename)
        result = self.recognizer.__process_sample(sample)
        self.assertEqual(number, result)

    def test_process_image_search_numbers(self):
        filename = 'img/all_numbers.png'
        result = self.recognizer.process_image(filename).getResult()
        self.assertEqual("987654321", result)


if __name__ == '__main__':
    unittest.main()
