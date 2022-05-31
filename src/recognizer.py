from src.domain.pattern_builder import PatternBuilder
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()

    def recognize(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        # Data acquisition Stage
        target_image = PatternBuilder.build_target(target_filename)
        patterns = [PatternBuilder.build_pattern(number_name, patterns_filename) for number_name in range(10)]
        answer = self.recognize_patterns(target_image, patterns)
        return answer, patterns

    def recognize_patterns(self, target_image_pattern, patterns):
        """ Stages of Segmentation / Representation / Classification """
        answer = self.recognizer.process_image(target_image_pattern, patterns)
        return answer

