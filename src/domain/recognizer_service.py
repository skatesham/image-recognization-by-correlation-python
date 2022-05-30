from src.domain.pixel_reader import PixelReader
from src.domain.recognizer_module import RecognizerModule


class RecognizerService:

    def __init__(self) -> None:
        super().__init__()
        self.recognizer_module = RecognizerModule()
        self.reader = PixelReader()

    def process_image(self, process):
        ''' Process the following stages of image processing
        Segmentation / Representation / Classification '''
        # Segmentation Stage
        while process.pointer.end_pointer_y <= process.height:
            sample_result = self.__segmentation_stage_unitary(process)
            process.answer += sample_result
        return process

    def __segmentation_stage_unitary(self, process):
        ''' Extract segments (samples) of the target_image
        based on the pattern image '''
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
        process.pointer.next(answer)
        return answer

    def __representation_stage(self, target_sample, process):
        ''' Stage of process all patterns with the segment (sample) '''
        best_result = -2
        best_pattern = ''
        for pattern in process.patterns:
            result = self.recognizer_module.represent(pattern.pixels, target_sample)
            pattern.results.append(result)
            if result > best_result:
                best_result = result
                best_pattern = pattern

        # Classification Stage
        if self.__classify_pattern(best_result, best_pattern.success_marge):
            best_pattern.best_result = best_result
            best_pattern.delta_y = process.pointer.init_pointer_y
            best_pattern.delta_x = process.pointer.init_pointer_x
            return str(best_pattern.name)

        return str()

    def __classify_pattern(self, result, success_marge):
        ''' Stage of filter the positive results '''
        return result > success_marge

