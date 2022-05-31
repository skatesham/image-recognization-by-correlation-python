from operator import attrgetter

from src.domain.correlation_utils import CorrelationUtils
from src.domain.model.result import Result


class RepresentationModule:

    @staticmethod
    def represent_results(target_segments, patterns):
        results = dict((pattern, list()) for pattern in patterns)
        for segment in target_segments:
            for pattern in patterns:
                pattern_results = results[pattern]
                result_value = CorrelationUtils.calculate_correlation(pattern.pixels, segment.pixels)
                result = Result(result_value, segment.delta_x, segment.delta_y, pattern.class_name)
                pattern_results.append(result)
        for key in results:
            results[key].sort(key=attrgetter('value'), reverse=True)
        return results
