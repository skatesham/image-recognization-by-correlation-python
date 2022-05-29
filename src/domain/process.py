from src.domain.pixel_pointer import PixelPointer


class Process:
    def __init__(self, matriz, width, height, pattern_width, pattern_height, success_marge=0.88) -> None:
        super().__init__()
        # higher error found on correlation matriz was 0.87
        self.success_marge = success_marge  # 0.88 was lucky number, for first sample examples
        self.matriz = matriz
        self.width = width
        self.height = height
        self.number_patterns = range(10)

        self.pattern_width = pattern_width
        self.pattern_height = pattern_height

        self.results = dict((pattern, []) for pattern in self.number_patterns)
        self.filtered_results = dict((pattern, []) for pattern in self.number_patterns)
        self.best_results = dict((pattern, []) for pattern in self.number_patterns)
        self.full_answer = str()

        self.pointer = PixelPointer(height, width, self.pattern_height, self.pattern_width)

    def getResults(self):
        return self.results

    def getFilteredResults(self, size_best_results=5):
        for pattern in self.number_patterns:
            self.results[pattern].sort()
            self.filtered_results[pattern] = self.results[pattern][-size_best_results:]

        return self.filtered_results

    def getBestResult(self):
        return self.best_results

    def getAnswer(self):
        return self.full_answer
