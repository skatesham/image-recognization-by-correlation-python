from src.domain.model.pattern import Pattern
from src.domain.processing.pixel_reader import PixelReaderUtils


class PatternBuilder:

    @staticmethod
    def build_pattern(name, patterns_filename):
        pixels, pattern_width, pattern_height = PixelReaderUtils.read_as_list(patterns_filename.format(name))
        return Pattern(name, pixels, pattern_height, pattern_width)

    @staticmethod
    def build_target(target_filename):
        pixels, pattern_width, pattern_height = PixelReaderUtils.read_as_matriz(target_filename)
        return Pattern(target_filename, pixels, pattern_height, pattern_width)
