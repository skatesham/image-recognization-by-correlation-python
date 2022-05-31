class Result:
    def __init__(self, value, delta_x, delta_y, class_name) -> None:
        super().__init__()
        self.value = value
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.class_name = class_name

    def __str__(self) -> str:
        return f"f({self.delta_x}, {self.delta_y})={self.value}"
