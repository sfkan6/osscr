from ..image_detection.cv2_detection.object_detection import Contour, Processor, MultipleProcessor
from ..image_detection import RectangleContour
from ..image_detection.processors import (
    ContourToRectangle, RectangleSorterProcessor, 
    AspectRatioProcessor, RectangleSorterProcessor, 
    RectangleMergingProcessor, PositionProcessor
)



class RectangleIncreaser(Processor):
    def __init__(self, increase_in_height, increase_in_width):
        self._increase_in_height = increase_in_height // 2
        self._increase_in_width = increase_in_width // 2
   
    def get_contours(self, contours: list, height=0, width=0):
        return [self.get_increase_rectangle(contour) for contour in contours]

    def get_increase_rectangle(self, rectangle: RectangleContour):
        x, y, width, height = rectangle.bounding_rect
        rectangle.set_bounding_rect(
            max(0, x - self._increase_in_width),
            max(0, y - self._increase_in_height),
            width + self._increase_in_width,
            height + self._increase_in_height,
        )
        return rectangle


class NestedRectanglesMergingProcessor(RectangleMergingProcessor):
    
    def get_merged_rectangles_if(self, rect1: RectangleContour, rect2: RectangleContour):
        if self.is_nested_by_x(rect1, rect2):
            return super().get_merged_rectangles_if(rect1, rect2)

    def is_nested_by_x(self, rect1: RectangleContour, rect2: RectangleContour):
        if rect1.x <= rect2.x and rect1.x + rect1.width >= rect2.x + rect2.width:
            return True
        return False


class VerticalPositionProcessor(PositionProcessor):
    
    def __init__(self):
        super().__init__(hw_min=1, hw_max=8)


class RectangleAspectRatioProcessor(AspectRatioProcessor):
    def __init__(self, n_width=0.1, n_height=0.4):
        super().__init__(n_width, n_height)
    
    def is_correct_contour(self, contour: Contour):
        if self.is_height_more_n_percent(contour):
            return True
        return False


class CharacterRectangleProcessor(MultipleProcessor):
    def __init__(self):
        processors = [
            ContourToRectangle(),
            NestedRectanglesMergingProcessor(),
            VerticalPositionProcessor(),
            RectangleAspectRatioProcessor(),
            RectangleIncreaser(increase_in_width=3, increase_in_height=6),
            RectangleSorterProcessor(0)
        ]
        super().__init__(processors)

