class Result:
    def __init__(self, value, delta_x, delta_y) -> None:
        super().__init__()
        self.value = value
        self.delta_x = delta_x
        self.delta_y = delta_y

    def __str__(self) -> str:
        return self.value

