import sys

from src.domain.acquisition_module import AcquisitionModule
from src.recognizer_service import RecognizerService


class RecognizerApplication:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()

    def recognize(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        return self.recognizer.process_image(target_filename, patterns_filename)

    def recognize_patterns(self, target_image_pattern, patterns):
        """ Stages of Segmentation / Representation / Classification """
        answer = self.recognizer.process_image_without_acquisition(target_image_pattern, patterns)
        return answer

