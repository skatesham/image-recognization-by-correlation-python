from src.domain.model.pattern import Pattern
from src.domain.utils.pixel_reader import PixelReaderUtils


class PatternTemplates:

    @staticmethod
    def build_patterns(patterns_filename="../resources/img/numbers/{}.png"):
        return [PatternTemplates.build_pattern_number(i, patterns_filename) for i in range(10)]

    @staticmethod
    def build_pattern_0(patterns_filename="../resources/img/numbers/{}.png"):
        return PatternTemplates.build_pattern_number(0, patterns_filename)

    @staticmethod
    def build_pattern_number(number, patterns_filename="../resources/img/numbers/{}.png"):
        pixels, pattern_width, pattern_height = PixelReaderUtils.read_as_list(patterns_filename.format(number))
        return Pattern(number, pixels, pattern_height, pattern_width)

    @staticmethod
    def build_target_all_numbers():
        target_filename = 'img/all_numbers.png'
        pixels, pattern_width, pattern_height = PixelReaderUtils.read_as_matriz(target_filename)
        return Pattern(target_filename, pixels, pattern_height, pattern_width)
