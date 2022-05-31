from src.domain.processing.classification_module import ClassificationModule
from src.domain.processing.representation_module import RepresentationModule
from src.domain.processing.segmentation_module import SegmentationModule


class RecognizerService:

    def __init__(self) -> None:
        super().__init__()
        self.segmentation_module = SegmentationModule()
        self.representation_module = RepresentationModule()
        self.classification_module = ClassificationModule()

    def process_image(self, target_image, patterns):
        ''' Process the following stages of image processing
        Segmentation / Representation / Classification '''
        first_pattern = patterns[0]
        target_segments = SegmentationModule.extract_segments(target_image, first_pattern)
        results = RepresentationModule.represent_results(target_segments, patterns)
        answer = ClassificationModule.classify_results(results, patterns)
        return answer
