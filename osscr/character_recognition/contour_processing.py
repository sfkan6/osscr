from ..image_detection.processors import (
    Contour, RectangleContour, Processor, MultipleProcessor,
    RectangleSorterProcessor, AspectRatioProcessor, 
    RectangleSorterProcessor, RectangleMergingProcessor, 
    PositionProcessor
)



class RectangleIncreaser(Processor):
    def __init__(self, increase_in_height, increase_in_width):
        self._increase_in_height = increase_in_height // 2
        self._increase_in_width = increase_in_width // 2
    
    def get_contours(self, contours: list[Contour], height: int | float = 0, width: int | float = 0) -> list[Contour]:
        return [self.get_increase_rectangle(contour) for contour in contours]

    def get_increase_rectangle(self, contour: Contour):
        x, y, width, height = contour.bounding_rect
        return RectangleContour(
            max(0, x - self._increase_in_width),
            max(0, y - self._increase_in_height),
            width + self._increase_in_width,
            height + self._increase_in_height,
        )


class NestedRectanglesMergingProcessor(RectangleMergingProcessor):
   
    def get_merged_rectangles_if(self, rect1: Contour, rect2: Contour) -> RectangleContour | None:
        if self.is_nested_by_x(rect1, rect2):
            return super().get_merged_rectangles_if(rect1, rect2)
    
    def is_nested_by_x(self, rect1: Contour, rect2: Contour):
        x1, _, w1, _ = rect1.bounding_rect
        x2, _, w2, _ = rect2.bounding_rect
        if x1 <= x2 and x1 + w1 >= x2 + w2:
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


class CharacterProcessor(MultipleProcessor):
    def __init__(self):
        processors = [
            NestedRectanglesMergingProcessor(),
            VerticalPositionProcessor(),
            RectangleAspectRatioProcessor(),
            RectangleIncreaser(increase_in_width=3, increase_in_height=6),
            RectangleSorterProcessor(0)
        ]
        super().__init__(processors)

