import unittest

from src.domain.processing.segmentation_module import SegmentationModule
from tests.pattern_templates import PatternTemplates


class SegmentationModuleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_extract_segments(self):
        pattern = PatternTemplates.build_pattern_0()
        target_image = PatternTemplates.build_target_all_numbers()
        segments = SegmentationModule.extract_segments(target_image, pattern)
        self.assertEqual(84, len(segments))
        self.assertEqual(252, len(segments[0].pixels))
        self.assertEqual(0, segments[0].delta_x)
        self.assertEqual(0, segments[0].delta_y)
        self.assertEqual(1, segments[1].delta_x)
        self.assertEqual(0, segments[1].delta_y)


if __name__ == '__main__':
    unittest.main()
