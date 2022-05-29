from src.domain.pixel_reader import PixelReader
from src.domain.process import Process
from src.domain.recognizer_module import RecognizerModule


class RecognizerService:

    def __init__(self) -> None:
        super().__init__()
        self.processor = RecognizerModule()
        self.reader = PixelReader()

    def process_image(self, process):
        answer = str()
        # Extract and recognize all patterns numbers on image using a pointer class
        while process.pointer.end_pointer_y <= process.height:
            sample_result = self.__extract_and_process_sample(process)
            answer += sample_result
        process.full_answer = answer
        return process

    def __extract_and_process_sample(self, process):
        sample = []
        y = process.pointer.init_pointer_y
        while y < process.pointer.end_pointer_y:
            x = process.pointer.init_pointer_x
            while x < process.pointer.end_pointer_x:
                sample.append(process.matriz[y][x])
                x += 1
            y += 1
        answer = self.__process_all_numbers_on_sample(sample, process)
        if answer != str():
            # Found pattern on sample
            process.pointer.init_on_next_pattern()
            return answer
        else:
            # Not found pattern on sample
            process.pointer.init_on_next_pixel()
            return str()

    def __process_all_numbers_on_sample(self, sample, process):
        best_result = -2
        best_pattern = ''
        for pattern in process.number_patterns:  # number_patterns  = range(10)
            result = self.__recognize_pattern(pattern, sample, process.pattern_paths_format)
            process.results[pattern].append(result)
            if result > best_result:
                best_result = result
                best_pattern = pattern

        if self.__check_recognition(best_result, process.success_marge):
            process.best_results[best_pattern].append(best_result)
            return str(best_pattern)

        return str()

    def __recognize_pattern(self, pattern_number, image_sample, pattern_paths_format):
        pattern_file_name = pattern_paths_format.format(pattern_number)
        pixels, width, height = self.reader.read_with_size(pattern_file_name)
        self.processor.withPixels(pixels, width, height)
        self.processor.correlatePattern(image_sample)
        return self.processor.getCorrelationResult()

    def __check_recognition(self, result, success_marge):
        return result > success_marge
