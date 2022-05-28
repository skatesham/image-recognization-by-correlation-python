from src.correlation_processor import CorrelationProcessor
from src.image_reader import ImageReader


class ImageRecognizer:

    def __init__(self) -> None:
        super().__init__()
        # higher error found on correlation matriz was 0.87
        self.error_marge = 0.9
        self.processor = CorrelationProcessor()
        self.processor.withImageFlat(f"../resources/img/numbers/{0}.png")
        self.reader = ImageReader()

    def process_image(self, filename):
        a_width = self.processor.pattern_width
        a_height = self.processor.pattern_height
        matriz, width, height = self.reader.read(filename)

        sample = self.extract_sample(a_height, a_width, height, matriz, width)
        processed_sample = self.process_sample(sample)

        #return "9876543210"
        return processed_sample

    def extract_sample(self, a_height, a_width, height, matriz, width):
        sample = []
        y = 0
        pointer_y = a_height
        pointer_x = a_width
        while y < height:
            if y >= pointer_y:
                break
            x = 0
            while x < width:
                if x >= pointer_x:
                    break
                sample.append(matriz[y][x])
                x += 1
            y += 1
        return sample

    def process_sample(self, sample):
        for i in range(10):
            result = self.correlate(i, sample)
            if self.check_recognition(result):
                return str(i)

        return str()

    def correlate(self, pattern_number, image_sample):
        pattern_file_name = "../resources/img/numbers/" + str(pattern_number) + ".png"
        self.processor.withImageFlat(pattern_file_name)
        self.processor.correlatePattern(image_sample)
        return self.processor.getCorrelationResult()

    def check_recognition(self, result):
        return result > self.error_marge
