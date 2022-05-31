from src.domain.processing.acquisition_module import AcquisitionModule
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()

    def recognize(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        target_image, patterns = AcquisitionModule.build_target_and_patterns(target_filename, patterns_filename)
        answer = self.recognizer.process_image_without_acquisition(target_image, patterns)
        return answer, patterns

    def recognize_patterns(self, target_image_pattern, patterns):
        """ Stages of Segmentation / Representation / Classification """
        answer = self.recognizer.process_image_without_acquisition(target_image_pattern, patterns)
        return answer

