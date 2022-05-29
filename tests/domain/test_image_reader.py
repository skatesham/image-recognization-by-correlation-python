import unittest

import numpy

from src.domain.img_reader import ImageReader


class ImageReaderTestCase(unittest.TestCase):

    def setUp(self):
        self.reader = ImageReader()

    def test_read_blank_image(self):
        read = self.reader.read("img/blank.png")
        expected = [[255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255]]
        self.assertEqual((expected, 5, 5), read)

    def test_read_flat_blank_image(self):
        read = self.reader.read_flat("img/blank.png")
        expected = [255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255]
        self.assertEqual(expected, read)
        self.assertEqual(expected, numpy.array(expected).tolist())

    def test_read_flat_chess_inline_image(self):
        read = self.reader.read_flat("img/chess-inline.png")
        expected = [0, 255, 0, 255, 0, 255, 0, 255, 0, 255]
        self.assertEqual(expected, read)
        self.assertEqual(expected, numpy.array(expected).tolist())


if __name__ == '__main__':
    unittest.main()
