from cv2_detection.object_detection import Contour, RectangleContour, Processor, MultipleProcessor


class AspectRatioProcessor(Processor):
    def __init__(self, n_width=0.1, n_height=0.1):
        self.n_height = n_height
        self.n_width = n_width
    
    def is_correct_contour(self, contour: Contour) -> bool:
        if self.is_more_n_percent(contour):
            return True
        return False

    def is_more_n_percent(self, contour: Contour):
        if (
            self.is_width_more_n_percent(contour) and
            self.is_height_more_n_percent(contour)
        ):
            return True
        return False

    def is_width_more_n_percent(self, contour: Contour):
        _, _, width, _= contour.bounding_rect
        if self.n_width <= width / self.width:
            return True
        return False

    def is_height_more_n_percent(self, contour: Contour):
        _, _, _, height = contour.bounding_rect
        if self.n_height <= height / self.height:
            return True
        return False


class RectangleMergingProcessor(Processor):
    
    def get_contours(self, contours: list[Contour], height: int | float = 0, width: int | float = 0) -> list[Contour]:
        i = 0
        while i < len(contours) - 1:
            new_rect = self.get_merged_rectangles_if(contours[i], contours[i + 1])
            if new_rect:
                contours[i] = new_rect
                contours.pop(i + 1)
                i -= 1
            i += 1
        return contours
    
    def get_merged_rectangles_if(self, rect1: Contour, rect2: Contour) -> RectangleContour|None:
        if True:
            return self.get_merged_rectangles(rect1, rect2)
        return None

    def get_merged_rectangles(self, rect1: Contour, rect2: Contour) -> RectangleContour:
        x1, y1, w1, h1 = rect1.bounding_rect
        x2, y2, w2, h2 = rect2.bounding_rect
        x, y = min(x1, x2), min(y1, y2)
        width = max(x1 + w1, x2 + w2) - x
        height = max(y1 + h1, y2 + h2) - y
        return RectangleContour(x, y, width, height)



class PositionProcessor(Processor):
    def __init__(self, hw_min, hw_max):
        self.hw_min = hw_min
        self.hw_max = hw_max
    
    def is_correct_contour(self, contour: Contour) -> bool:
        _, _, width, height = contour.bounding_rect
        if self.hw_min <= height / width <= self.hw_max:
            return True
        return False



class RectangleSorterProcessor(Processor):
    
    def __init__(self, side_index: int=0) -> None:
        self.side_index = side_index
    
    def get_contours(self, contours: list[Contour], height: int | float = 0, width: int | float = 0) -> list[Contour]:
        return sorted(contours, key=lambda contour: contour.bounding_rect[self.side_index])

