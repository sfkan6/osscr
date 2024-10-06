from ..image_detection.processors import (
    Contour, RectangleContour, MultipleProcessor,
    RectangleSorterProcessor, 
    AspectRatioProcessor, RectangleSorterProcessor, 
    RectangleMergingProcessor, PositionProcessor
)
import math


class CloseRectanglesMergingProcessor(RectangleMergingProcessor):

    def __init__(self, error_by_y=0.2):
        self.error_by_y = error_by_y
    
    def get_merged_rectangles_if(self, rect1: Contour, rect2: Contour) -> RectangleContour | None:
        if rect1.bounding_rect[0] > rect2.bounding_rect[0]:
            rect1, rect2 = rect2, rect1
        if (
            self.is_rectangles_on_same_level(rect1, rect2) 
            and
            self.is_rectangles_close_in_x(rect1, rect2)
        ):
            return super().get_merged_rectangles_if(rect1, rect2)
        return None

    def is_rectangles_on_same_level(self, left_rect: Contour, right_rect: Contour):
        _, y1, _, h1 = left_rect.bounding_rect
        _, y2, _, h2 = right_rect.bounding_rect
        if (
            abs(y1 - y2) < h1 * self.error_by_y and 
            abs(h1 - h2) < h1 * self.error_by_y
        ):
            return True
        return False

    def is_rectangles_close_in_x(self, left_rect: Contour, right_rect: Contour):
        x1, _, w1, h1 = left_rect.bounding_rect
        x2, _, _, h2 = right_rect.bounding_rect
        error_by_x = max(h1, h2)
        if abs(x2 - (x1 + w1)) < error_by_x:
            return True
        return False


class DisplayRatioProcessor(AspectRatioProcessor):
    def __init__(self, n_width=0.1, n_height=0.1):
        super().__init__(n_width, n_height)
    
    def is_correct_contour(self, contour: Contour) -> bool:
        if self.is_more_n_percent(contour):
            return True
        return False


class RadiusRectanglesMergingProcessor(RectangleMergingProcessor):
    
    def get_merged_rectangles_if(self, rect1: Contour, rect2: Contour) -> RectangleContour | None:
        if self.is_nested_by_radius(rect1, rect2):
            return super().get_merged_rectangles_if(rect1, rect2)

    def is_nested_by_radius(self, rect1: Contour, rect2: Contour):
        x1, y1, w1, h1 = rect1.bounding_rect
        x2, y2, w2, h2 = rect2.bounding_rect
        max_r = (math.sqrt(h1**2 + w1**2) + math.sqrt(h2**2 + w2**2)) / 2
        r = math.sqrt(((x1 + w1 / 2) - (x2 + w2 / 2))**2  + ((y1 + h1 / 2) - (y2 + h2 / 2))**2)
        if r <= max_r / 2:
            return True
        return False


class DisplayRectangleProcessor(MultipleProcessor):
    
    def __init__(self):
        processors = [
            RectangleSorterProcessor(0),
            RadiusRectanglesMergingProcessor(),
            DisplayRatioProcessor(n_height=0.05),
            CloseRectanglesMergingProcessor(),
        ]
        super().__init__(processors)

