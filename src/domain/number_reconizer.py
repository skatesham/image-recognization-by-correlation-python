from src.domain.pointer import ImagePointer
from src.domain.correlation_processor import CorrelationProcessor
from src.domain.img_reader import ImageReader


class NumberImageRecognizer:

    def __init__(self, success_marge=0.88) -> None:
        super().__init__()
        # higher error found on correlation matriz was 0.87
        self.success_marge = success_marge  # 0.88 was lucky number, for first sample examples
        self.processor = CorrelationProcessor()
        self.processor.withImageFlat(f"../resources/img/numbers/{0}.png")
        self.reader = ImageReader()
        self.pattern_width = self.processor.pattern_width
        self.pattern_height = self.processor.pattern_height
        self.results = str()

    def process_image(self, filename):
        # Read data from image target recognition
        matriz, width, height = self.reader.read(filename)
        results = str()
        # Extract and recognize all patterns numbers on image using a pointer class
        pointer = ImagePointer(height, width, self.pattern_height, self.pattern_width)
        while pointer.end_pointer_y <= height:
            sample_result = self.__extract_and_process_sample(matriz, pointer)
            results += sample_result
        self.results = results
        return self

    def getResult(self):
        return self.results

    def __extract_and_process_sample(self, matriz, pointer):
        sample = []
        y = pointer.init_pointer_y
        while y < pointer.end_pointer_y:
            x = pointer.init_pointer_x
            while x < pointer.end_pointer_x:
                sample.append(matriz[y][x])
                x += 1
            y += 1
        result = self.__process_all_numbers_on_sample(sample)
        if result != str():
            # Found pattern on sample
            pointer.init_on_next_pattern()
            return result
        else:
            # Not found pattern on sample
            pointer.init_on_next_pixel()
            return str()

    def __process_all_numbers_on_sample(self, sample):
        for i in range(10):  # Pattern numbers 0 to 9
            result = self.__recognize_pattern(i, sample)
            if self.__check_recognition(result):
                return str(i)

        return str()

    def __recognize_pattern(self, pattern_number, image_sample):
        pattern_file_name = "../resources/img/numbers/" + str(pattern_number) + ".png"
        self.processor.withImageFlat(pattern_file_name)
        self.processor.correlatePattern(image_sample)
        return self.processor.getCorrelationResult()

    def __check_recognition(self, result):
        return result > self.success_marge
