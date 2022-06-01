from src.domain.acquisition_module import AcquisitionModule
from src.domain.classification_module import ClassificationModule
from src.domain.representation_module import RepresentationModule
from src.domain.segmentation_module import SegmentationModule


class RecognizerService:

    @staticmethod
    def process_image(target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        target_image, patterns = AcquisitionModule.build_target_and_patterns(target_filename, patterns_filename)
        target_segments = SegmentationModule.extract_segments(target_image, patterns[0])
        results = RepresentationModule.represent_results(target_segments, patterns)
        answer = ClassificationModule.classify_results(results, patterns)
        return answer

    @staticmethod
    def process_image_without_acquisition(target_image, patterns):
        ''' Execute the image processing modules '''
        first_pattern = patterns[0]
        target_segments = SegmentationModule.extract_segments(target_image, first_pattern)
        results = RepresentationModule.represent_results(target_segments, patterns)
        answer = ClassificationModule.classify_results(results, patterns)
        return answer
