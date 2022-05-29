from src.domain.number_reconizer import NumberImageRecognizer


class RecImgUseCase():

    def __init__(self) -> None:
        super().__init__()
        self.recognizer = NumberImageRecognizer()
