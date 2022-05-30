from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_module import RecognizerModule


class RecognizerService:

    def __init__(self) -> None:
        super().__init__()
        self.processor = RecognizerModule()
        self.reader = PixelReader()

    def process_image(self, process):
        process.answer = self.__segmentation_stage(process)
        return process

    def __segmentation_stage(self, process):
        answer = ''
        while process.pointer.end_pointer_y <= process.height:
            sample_result = self.__segment_sample(process)
            answer += sample_result
        return answer

    def __segment_sample(self, process):
        sample = []
        delta_y = process.pointer.init_pointer_y
        while delta_y < process.pointer.end_pointer_y:
            delta_x = process.pointer.init_pointer_x
            while delta_x < process.pointer.end_pointer_x:
                sample.append(process.pixels[delta_y][delta_x])
                delta_x += 1
            delta_y += 1
        # Representation Stage
        answer = self.__representation_stage(sample, process)
        if answer != str():
            # Found pattern on target_sample
            process.pointer.init_on_next_pattern()
            return answer
        else:
            # Not found pattern on target_sample
            process.pointer.init_on_next_pixel()
            return str()

    def __representation_stage(self, target_sample, process):
        best_result = -2
        best_pattern = ''
        for pattern in process.patterns:
            result = self.__represent_pattern(pattern.pixels, target_sample)
            pattern.results.append(result)
            if result > best_result:
                best_result = result
                best_pattern = pattern

        # Classification Stage
        if self.__classify_pattern(best_result, best_pattern.success_marge):
            best_pattern.best_result = best_result
            return str(best_pattern.name)

        return str()

    def __represent_pattern(self, pattern, target_sample):
        result = self.processor.represent(pattern, target_sample)
        return float("{:.2f}".format(result))

    def __classify_pattern(self, result, success_marge):
        return result > success_marge
