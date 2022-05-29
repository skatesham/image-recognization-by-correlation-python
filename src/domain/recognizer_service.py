from src.domain.recognizer_module import RecognizerModule
from src.domain.img_reader import ImageReader
from src.domain.pointer import ImagePointer


class RecognizerProcessor:

    def __init__(self, success_marge=0.88) -> None:
        super().__init__()
        # higher error found on correlation matriz was 0.87
        self.success_marge = success_marge  # 0.88 was lucky number, for first sample examples
        self.processor = RecognizerModule()
        self.number_patterns = range(10)
        self.processor.withImageFlat(f"../resources/img/numbers/{self.number_patterns[0]}.png")
        self.reader = ImageReader()
        self.pattern_width = self.processor.pattern_width
        self.pattern_height = self.processor.pattern_height
        self.results = dict((pattern, []) for pattern in self.number_patterns)
        self.filtered_results = dict((pattern, []) for pattern in self.number_patterns)
        self.best_results = dict((pattern, []) for pattern in self.number_patterns)
        self.full_answer = str()

    def process_image(self, filename):
        # Read data from image target recognition
        matriz, width, height = self.reader.read(filename)
        answer = str()
        # Extract and recognize all patterns numbers on image using a pointer class
        pointer = ImagePointer(height, width, self.pattern_height, self.pattern_width)
        while pointer.end_pointer_y <= height:
            sample_result = self.__extract_and_process_sample(matriz, pointer)
            answer += sample_result
        self.full_answer = answer
        return self

    def getResults(self):
        return self.results

    def getFilteredResults(self, size_best_results=5):

        for pattern in self.number_patterns:
            self.results[pattern].sort()
            self.filtered_results[pattern] = self.results[pattern][-size_best_results:]

        return self.filtered_results

    def getBestResult(self):
        return self.best_results

    def getAnswer(self):
        return self.full_answer

    def __extract_and_process_sample(self, matriz, pointer):
        sample = []
        y = pointer.init_pointer_y
        while y < pointer.end_pointer_y:
            x = pointer.init_pointer_x
            while x < pointer.end_pointer_x:
                sample.append(matriz[y][x])
                x += 1
            y += 1
        answer = self.__process_all_numbers_on_sample(sample)
        if answer != str():
            # Found pattern on sample
            pointer.init_on_next_pattern()
            return answer
        else:
            # Not found pattern on sample
            pointer.init_on_next_pixel()
            return str()

    def __process_all_numbers_on_sample(self, sample):
        best_result = -2
        best_pattern = ''
        for pattern in self.number_patterns:  # number_patterns  = range(10)
            result = self.__recognize_pattern(pattern, sample)
            self.results[pattern].append(result)
            if result > best_result:
                best_result = result
                best_pattern = pattern

        if self.__check_recognition(best_result):
            self.best_results[best_pattern].append(best_result)
            return str(best_pattern)

        return str()

    def __recognize_pattern(self, pattern_number, image_sample):
        pattern_file_name = f"../resources/img/numbers/{ pattern_number }.png"
        self.processor.withImageFlat(pattern_file_name)
        self.processor.correlatePattern(image_sample)
        return self.processor.getCorrelationResult()

    def __check_recognition(self, result):
        return result > self.success_marge
