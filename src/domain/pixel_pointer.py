class PixelPointer:

    def __init__(self, max_height, max_width, pattern_height, pattern_width) -> None:
        super().__init__()
        self.__max_height = max_height
        self.__max_width = max_width
        self.pattern_height = pattern_height
        self.pattern_width = pattern_width
        self.init_pointer_y = 0
        self.init_pointer_x = 0
        self.end_pointer_y = self.pattern_height
        self.end_pointer_x = self.pattern_width

    def next(self, answer):
        if answer != '':
            # Found pattern on target_sample
            self.init_on_next_pattern()

        else:
            # Not found pattern on target_sample
            self.init_on_next_pixel()
        self.__update_y_when_needed()

    def init_on_next_pattern(self):
        self.init_pointer_x += int(self.pattern_width * 0.3)
        self.end_pointer_x = self.init_pointer_x + self.pattern_width

    def init_on_next_pixel(self):
        self.init_pointer_x += 1
        self.end_pointer_x = self.init_pointer_x + self.pattern_width

    def __update_y_when_needed(self):
        if self.end_pointer_x > self.__max_width:
            self.init_pointer_x = 0
            self.end_pointer_x = self.pattern_width

            self.init_pointer_y = int(self.end_pointer_y * 0.5)
            self.end_pointer_y = self.init_pointer_y + self.pattern_height
