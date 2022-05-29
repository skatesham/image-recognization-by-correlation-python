from src.domain.recognizer_service import RecognizerProcessor


class RecImgUseCase:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = RecognizerProcessor()

    def recognize_patterns_v1(self, filename):
        return self.recognizer.process_image(filename).getAnswer()