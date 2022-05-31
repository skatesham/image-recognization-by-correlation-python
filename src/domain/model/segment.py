class Segment:

    def __init__(self, pixels, delta_x, delta_y) -> None:
        super().__init__()
        self.pixels = pixels
        self.delta_x = delta_x
        self.delta_y = delta_y
