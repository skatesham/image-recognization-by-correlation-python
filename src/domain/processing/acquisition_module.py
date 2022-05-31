from src.domain.builder.pattern_builder import PatternBuilder


class AcquisitionModule:

    @staticmethod
    def build_target_and_patterns(target_filename, patterns_filename):
        # Data acquisition Stage
        target_image = PatternBuilder.build_target(target_filename)
        patterns = [PatternBuilder.build_pattern(number_name, patterns_filename) for number_name in range(10)]
        return target_image, patterns
