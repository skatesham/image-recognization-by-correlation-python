import json

from src.domain.pixel_pointer import PixelPointer


class Process:
    def __init__(self, target_image, patterns) -> None:
        super().__init__()

        self.target_pattern = target_image
        self.patterns = patterns

        # this approach only allow same width pattern,
        # but if not must get other size o samples also
        self.pattern_width = patterns[0].width
        self.pattern_height = patterns[0].height

        self.answer = str()
        self.pointer = PixelPointer(target_image.height, target_image.width, self.pattern_height, self.pattern_width)

    def get_results(self):
        return dict((pattern.name, pattern.get_results()) for pattern in self.patterns)

    def get_filtered_results(self, size_best_results=5):
        return dict((pattern.name, pattern.get_filtered_results(size_best_results)) for pattern in self.patterns)

    def get_best_results(self):
        return dict((pattern.name, pattern.best_result) for pattern in self.patterns)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)