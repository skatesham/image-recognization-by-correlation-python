from src.domain.pixel_pointer import PixelPointer
from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_module import RecognizerModule
from src.domain.result import Result


class RecognizerService:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer_module = RecognizerModule()
        self.reader = PixelReader()

    def process_image(self, target_image, patterns):
        ''' Process the following stages of image processing
        Segmentation / Representation / Classification '''
        # Segmentation Stage
        answer = ''
        pointer = PixelPointer(target_image.height, target_image.width, patterns[0].height, patterns[0].width)
        while pointer.end_pointer_y <= target_image.height:
            sample_result = self.__segmentation_stage_unitary(target_image, patterns, pointer)
            answer += sample_result
        return answer, patterns

    def __segmentation_stage_unitary(self, target_image, patterns, pointer):
        ''' Extract segments (samples) of the target_image
        based on the pattern image '''
        sample = []
        delta_y = pointer.init_pointer_y
        while delta_y < pointer.end_pointer_y:
            delta_x = pointer.init_pointer_x
            while delta_x < pointer.end_pointer_x:
                sample.append(target_image.pixels[delta_y][delta_x])
                delta_x += 1
            delta_y += 1
        # Representation Stage
        answer = self.__representation_stage(sample, patterns, pointer.init_pointer_y, pointer.init_pointer_x)
        pointer.next(answer)
        return answer

    def __representation_stage(self, target_sample, patterns, delta_x, delta_y):
        ''' Stage of process all patterns with the segment (sample) '''
        best_result = Result(-2, 0, 0)
        best_pattern = {}
        for pattern in patterns:
            result_value = self.recognizer_module.represent(pattern.pixels, target_sample)
            result = Result(result_value, delta_x, delta_y)
            pattern.results.append(result)
            if result_value > best_result.value:
                best_result = result
                best_pattern = pattern

        # Classification Stage
        if self.__classify_pattern(best_result, best_pattern.success_marge):
            best_pattern.best_result = best_result
            return str(best_pattern.name)

        return str()

    def __classify_pattern(self, result, success_marge):
        ''' Stage of filter the positive results '''
        return result.value > success_marge

