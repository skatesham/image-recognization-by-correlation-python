import unittest

from src.domain.processing.classification_module import ClassificationModule
from src.domain.processing.representation_module import RepresentationModule
from src.domain.processing.segmentation_module import SegmentationModule
from tests.pattern_templates import PatternTemplates


class RepresentationModuleTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_extract_segments(self):
        patterns = PatternTemplates.build_patterns()
        target_image = PatternTemplates.build_target_all_numbers()
        target_segments = SegmentationModule.extract_segments(target_image, patterns[0])
        results = RepresentationModule.represent_results(target_segments, patterns)
        answer = ClassificationModule.classify_results(results, patterns)
        self.assertEqual("987654321", answer)

    def to_less_results(self, result):
        return [str(r) for r in result[:2]]


if __name__ == '__main__':
    unittest.main()
