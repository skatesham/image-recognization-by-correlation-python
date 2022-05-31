from operator import attrgetter


class Pattern:
    def __init__(self, name, pixels, height, width, success_marge=0.88) -> None:
        super().__init__()
        self.name = name
        self.pixels = pixels
        self.height = height
        self.width = width
        self.success_marge = success_marge

        # TODO
        self.filename = ""

        self.results = list()
        self.best_result = {}

    def get_best_result(self):
        return self.best_result

    def get_results(self):
        return self.results

    def find_filtered_results(self, size_best_results=5):
        self.results.sort(key=attrgetter('value'), reverse=True)
        return self.results[-size_best_results:]
