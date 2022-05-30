import numpy


class RecognizerModule:

    def represent(self, pattern_pixels, target_pixels):
        ''' Calculate with correlation / coeficient of Pearson '''
        result = numpy.corrcoef(target_pixels, pattern_pixels).tolist()
        # Using just single result of correlation
        correlation_x_with_y = result[0][1]
        return float("{:.2f}".format(correlation_x_with_y))

