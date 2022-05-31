from src.domain.processing.segment import Segment
from src.domain.processing.segmentation_pointer import SegmentationPointer


class SegmentationModule:

    @staticmethod
    def extract_segments(target_image, pattern):
        pointer = SegmentationPointer(target_image.height, target_image.width, pattern.height, pattern.width)
        segments = []
        while pointer.end_pointer_y <= target_image.height:
            segment = SegmentationModule.__extract_segment(target_image, pointer)
            segments.append(segment)
        return segments

    @staticmethod
    def __extract_segment(target_image, pointer):
        ''' Extract segments (samples) of the target_image_pattern
        based on the pattern image '''
        pixels = []
        delta_y = pointer.init_pointer_y
        while delta_y < pointer.end_pointer_y:
            delta_x = pointer.init_pointer_x
            while delta_x < pointer.end_pointer_x:
                pixels.append(target_image.pixels[delta_y][delta_x])
                delta_x += 1
            delta_y += 1
        segment = Segment(pixels, pointer.init_pointer_x, pointer.init_pointer_y)
        SegmentationModule.init_on_next_pixel(pointer)
        return segment

    @staticmethod
    def init_on_next_pixel(pointer):
        pointer.init_pointer_x += 1
        pointer.end_pointer_x = pointer.init_pointer_x + pointer.pattern_width
        if pointer.end_pointer_x > pointer.max_width:
            pointer.init_pointer_x = 0
            pointer.end_pointer_x = pointer.pattern_width

            pointer.init_pointer_y = int(pointer.end_pointer_y * 0.5)
            pointer.end_pointer_y = pointer.init_pointer_y + pointer.pattern_height
