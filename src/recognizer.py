from src.domain.pixel_reader import PixelReader
from src.domain.process import Process
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()
        self.reader = PixelReader()

    def recognize_patterns(self, filename, pattern_paths_format="../resources/img/numbers/{}.png"):
        __, pattern_width, pattern_height = self.reader.read(pattern_paths_format.format(0))
        matriz, width, height = self.reader.read(filename)
        process = Process(matriz, width, height, pattern_width, pattern_height, pattern_paths_format)
        return self.recognizer.process_image(process)
