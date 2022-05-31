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
        # Acquisition Stage
        process = self.acquisition(target_filename, patterns_filename)
        # Segmentation / Representation / Classification Stage
        return self.recognizer.process_image(process)

    def acquisition(self, target_filename, patterns_filename="../resources/img/numbers/{}.png"):
        ''' Stage of obtain image data for processing '''
        target_matriz_pixels, width, height = self.reader.read_as_matriz(target_filename)
        target_image = Pattern(target_filename, target_matriz_pixels, height, width)
        patterns = list()
        for name in range(10):
            pixels, pattern_width, pattern_height = self.reader.read_as_list(patterns_filename.format(name))
            pattern = Pattern(name, pixels, pattern_height, pattern_width)
            patterns.append(pattern)
        return Process(target_image, patterns)

