import unittest

from src.domain.representation_module import RepresentationModule
from src.domain.segmentation_module import SegmentationModule
from tests.pattern_templates import PatternTemplates


class RepresentationModuleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_extract_segments(self):
        patterns = PatternTemplates.build_patterns()
        target_image = PatternTemplates.build_target_all_numbers()
        target_segments = SegmentationModule.extract_segments(target_image, patterns[0])
        results = RepresentationModule.represent_results(target_segments, patterns)
        self.assertEqual(10, len(results))
        expected_first_two_results = [
            ['f(0, 0)=0.85', 'f(31, 0)=0.83'],
            ['f(82, 0)=1.0', 'f(53, 0)=0.62'],
            ['f(72, 0)=0.98', 'f(71, 0)=0.83'],
            ['f(61, 0)=0.89', 'f(62, 0)=0.89'],
            ['f(51, 0)=0.97', 'f(52, 0)=0.8'],
            ['f(41, 0)=1.0', 'f(31, 0)=0.88'],
            ['f(31, 0)=0.97', 'f(10, 0)=0.86'],
            ['f(20, 0)=0.91', 'f(21, 0)=0.89'],
            ['f(10, 0)=0.97', 'f(31, 0)=0.87'],
            ['f(0, 0)=1.0', 'f(10, 0)=0.77']
        ]
        self.assertEqual(expected_first_two_results, [self.to_less_results(results[key]) for key in results])

    def to_less_results(self, result):
        return [str(r) for r in result[:2]]


if __name__ == '__main__':
    unittest.main()
