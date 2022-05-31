from operator import attrgetter


class Pattern:
    def __init__(self, name, pixels, height, width, success_marge=0.88) -> None:
        super().__init__()
        self.name = name
        self.pixels = pixels
        self.height = height
        self.width = width
        self.success_marge = success_marge
        self.best_result = ''
        self.delta_y = -1
        self.delta_x = -1

        self.results = list()
        self.filtered_results = list()

        self.delta_results = dict()

    def get_results(self):
        return self.results

    def get_filtered_results(self, size_best_results=5):
        self.results.sort(key=attrgetter('value'))
        return self.results[-size_best_results:]

    def get_best_result(self):
        return self.best_result
