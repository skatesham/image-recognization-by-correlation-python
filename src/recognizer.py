from src.domain.pattern_builder import PatternBuilder
from src.domain.pattern import Pattern
from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()
        self.reader = PixelReader()

    def recognize_patterns(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        # Data acquisition Stage
        target_image = PatternBuilder.build_target(target_filename)
        patterns = list()
        for name in range(10):
            pattern = PatternBuilder.build_pattern(name, patterns_filename)
            patterns.append(pattern)
        # Throw stages of Segmentation / Representation / Classification
        return self.recognizer.process_image(target_image, patterns)

