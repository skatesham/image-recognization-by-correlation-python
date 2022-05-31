from operator import attrgetter


class ClassificationModule:

    @staticmethod
    def classify_results(results, patterns):
        default_first_pattern_width = patterns[0].width
        positive_values = ClassificationModule.__filter_positives(results)
        filtered_results = ClassificationModule.__eliminate_duplicates(positive_values, default_first_pattern_width)
        return ''.join([x.class_name for x in filtered_results])

    @staticmethod
    def __filter_positives(results):
        positive_values = []
        for key in results:
            for result in results[key]:
                if ClassificationModule.__is_positive_pattern(result.value, result.success_marge):
                    positive_values.append(result)
        return positive_values

    @staticmethod
    def __is_positive_pattern(value, success_marge):
        ''' Check is positive based on success marge '''
        return value > success_marge

    @staticmethod
    def __eliminate_duplicates(positive_values, width):
        """ Eliminate the next result with half the width of a pattern """
        positive_values.sort(key=attrgetter('delta_x'))
        min_width = width // 2
        last_delta_x = -100
        filtered_results = []
        for result in positive_values:
            if result.delta_x - last_delta_x >= min_width:
                last_delta_x = result.delta_x
                filtered_results.append(result)
        return filtered_results
