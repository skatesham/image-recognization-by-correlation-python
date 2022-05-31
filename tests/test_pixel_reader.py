import unittest

import numpy

from src.domain.processing.pixel_reader import PixelReaderUtils


class ImageReaderTestCase(unittest.TestCase):

    def test_read_blank_image(self):
        read = PixelReaderUtils.read_as_matriz("img/blank.png")
        expected = [[255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255],
                    [255, 255, 255, 255, 255]]
        self.assertEqual((expected, 5, 5), read)

    def test_read_flat_blank_image(self):
        read = PixelReaderUtils.read_as_list("img/blank.png")
        expected = [255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255,
                    255, 255, 255, 255, 255]
        self.assertEqual((expected, 5, 5), read)
        self.assertEqual(expected, numpy.array(expected).tolist())

    def test_read_flat_chess_inline_image(self):
        read = PixelReaderUtils.read_as_list("img/chess-inline.png")
        expected = [0, 255, 0, 255, 0, 255, 0, 255, 0, 255]
        self.assertEqual((expected, 10, 1), read)
        self.assertEqual(expected, numpy.array(expected).tolist())


if __name__ == '__main__':
    unittest.main()
