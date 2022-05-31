from operator import attrgetter


class ClassificationModule:

    @staticmethod
    def classify_results(results, patterns):
        pattern = patterns[0]
        positive_values = ClassificationModule.__filter_positives(results, pattern.success_marge)
        filtered_results = ClassificationModule.__eliminate_duplicates(positive_values, pattern.width)
        return ''.join([x.class_name for x in filtered_results])

    @staticmethod
    def __filter_positives(results, success_marge):
        positive_values = []
        for key in results:
            for result in results[key]:
                if ClassificationModule.__is_positive_pattern(result.value, success_marge):
                    positive_values.append(result)
        positive_values.sort(key=attrgetter('delta_x'))
        return positive_values

    @staticmethod
    def __is_positive_pattern(value, success_marge):
        ''' Stage of filter the positive results '''
        return value > success_marge

    @staticmethod
    def __eliminate_duplicates(positive_values, width):
        min_width = width // 2
        last_delta_x = -100
        filtered_results = []
        for result in positive_values:
            if result.delta_x - last_delta_x >= min_width:
                last_delta_x = result.delta_x
                filtered_results.append(result)
        return filtered_results
