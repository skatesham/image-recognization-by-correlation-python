from operator import attrgetter

import numpy

from src.domain.model.result import Result

FORMAT_RESULT = "{:.2f}"


class RepresentationModule:

    @staticmethod
    def represent_results(target_segments, patterns):
        results = dict((pattern, list()) for pattern in patterns)
        for segment in target_segments:
            for pattern in patterns:
                pattern_results = results[pattern]
                value = RepresentationModule.calculate_correlation(pattern.pixels, segment.pixels)
                result = Result(value, segment.delta_x, segment.delta_y, pattern.class_name, pattern.success_marge)
                pattern_results.append(result)
        for key in results:
            results[key].sort(key=attrgetter('value'), reverse=True)
        return results

    @staticmethod
    def calculate_correlation(pattern_pixels, target_pixels):
        ''' Calculate correlation / coeficient of Pearson '''
        result = numpy.corrcoef(target_pixels, pattern_pixels).tolist()
        # Using just single result of correlation
        correlation_x_with_y = result[0][1]
        return float(FORMAT_RESULT.format(correlation_x_with_y))
