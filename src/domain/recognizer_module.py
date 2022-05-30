import numpy


class RecognizerModule:

    def represent(self, pattern_pixels, target_pixels):
        result = numpy.corrcoef(target_pixels, pattern_pixels).tolist()
        correlation_x_with_y = result[0][1]
        return float("{:.2f}".format(correlation_x_with_y))

