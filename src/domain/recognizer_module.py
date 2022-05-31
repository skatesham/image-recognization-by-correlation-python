import numpy

FORMAT_RESULT = "{:.2f}"


class RecognizerModule:

    @staticmethod
    def calculate_correlation(pattern_pixels, target_pixels):
        ''' Calculate with correlation / coeficient of Pearson '''
        result = numpy.corrcoef(target_pixels, pattern_pixels).tolist()
        # Using just single result of correlation
        correlation_x_with_y = result[0][1]
        return float(FORMAT_RESULT.format(correlation_x_with_y))
