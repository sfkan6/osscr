from ..image_detection import RectangleContour
from ..image_detection.cv2_detection import Contour, MultipleProcessor
from ..image_detection.processors import (
    ContourToRectangle, RectangleSorterProcessor, 
    AspectRatioProcessor, RectangleSorterProcessor, 
    RectangleMergingProcessor, PositionProcessor
)
import math

class CloseRectanglesMergingProcessor(RectangleMergingProcessor):

    def __init__(self, error_by_y=0.2):
        self.error_by_y = error_by_y
    
    def get_merged_rectangles_if(self, rect1: RectangleContour, rect2: RectangleContour) -> RectangleContour | None:
        if rect1.x > rect2.x:
            rect1, rect2 = rect2, rect1
        if (
            self.is_rectangles_on_same_level(rect1, rect2) 
            and
            self.is_rectangles_close_in_x(rect1, rect2)
        ):
            return super().get_merged_rectangles_if(rect1, rect2)

    def is_rectangles_on_same_level(self, left_rect: RectangleContour, right_rect: RectangleContour):
        if (
            abs(left_rect.y - right_rect.y) < left_rect.height * self.error_by_y and 
            abs(left_rect.height - right_rect.height) < left_rect.height * self.error_by_y
        ):
            return True
        return False

    def is_rectangles_close_in_x(self, left_rect: RectangleContour, right_rect: RectangleContour):
        error_by_x = max(left_rect.height, right_rect.height)
        if abs(right_rect.x - (left_rect.x + left_rect.width)) < error_by_x:
            return True
        return False


class DisplayRatioProcessor(AspectRatioProcessor):
    def __init__(self, n_width=0.1, n_height=0.1):
        super().__init__(n_width, n_height)
    
    def is_correct_contour(self, contour: Contour):
        if self.is_more_n_percent(contour):
            return True
        return False


class RadiusRectanglesMergingProcessor(RectangleMergingProcessor):
    
    def get_merged_rectangles_if(self, rect1: RectangleContour, rect2: RectangleContour):
        if self.is_nested_by_radius(rect1, rect2):
            return super().get_merged_rectangles_if(rect1, rect2)

    def is_nested_by_radius(self, rect1: RectangleContour, rect2: RectangleContour):
        max_r = (math.sqrt(rect1.height**2 + rect1.width**2) + math.sqrt(rect2.height**2 + rect2.width**2)) / 2
        r = math.sqrt(((rect1.x + rect1.width / 2) - (rect2.x + rect2.width / 2))**2  + ((rect1.y + rect1.height / 2) - (rect2.y + rect2.height / 2))**2)
        if r <= max_r / 2:
            return True
        return False


class DisplayRectangleProcessor(MultipleProcessor):
    
    def __init__(self):
        processors = [
            ContourToRectangle(),
            RectangleSorterProcessor(0),
            RadiusRectanglesMergingProcessor(),
            DisplayRatioProcessor(n_height=0.05),
            CloseRectanglesMergingProcessor(),
        ]
        super().__init__(processors)

