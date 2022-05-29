from src.domain.pixel_reader import PixelReader
from src.domain.process import Process
from src.domain.recognizer_service import RecognizerService


class Recognizer:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerService()
        self.reader = PixelReader()

    def recognize_patterns_v1(self, filename):
        # Read data from image target recognition
        __, pattern_width, pattern_height = self.reader.read(f"../resources/img/numbers/0.png")
        matriz, width, height = self.reader.read(filename)
        process = Process(matriz, width, height, pattern_width, pattern_height)
        return self.recognizer.process_image(process)
