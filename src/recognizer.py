from src.domain.pattern import Pattern
from src.domain.pixel_reader import PixelReader
from src.domain.process import Process
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()
        self.reader = PixelReader()

    def recognize_patterns(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        pixels, width, height = self.reader.read(target_filename)
        patterns = self.acquisition(patterns_filename)
        process = Process(pixels, width, height, patterns)
        return self.recognizer.process_image(process)

    def acquisition(self, patterns_filename="../resources/img/numbers/{}.png"):
        patterns = list()
        for name in range(10):
            pixels, width, height = self.reader.read_flat_with_size(patterns_filename.format(name))
            pattern = Pattern(name, pixels, height, width)
            patterns.append(pattern)
        return patterns

