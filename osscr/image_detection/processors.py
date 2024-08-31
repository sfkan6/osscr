from .cv2_detection import Contour, Processor
from .rectangle_contour import RectangleContour


class ContourToRectangle(Processor):

    def get_contours(self, contours: list, height=0, width=0):
        return [RectangleContour.create_by_contour(contour) for contour in contours]



class AspectRatioProcessor(Processor):
    def __init__(self, n_width=0.1, n_height=0.1):
        self.n_height = n_height
        self.n_width = n_width
    
    def is_correct_contour(self, contour: Contour):
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
        x, y, width, height = contour.bounding_rect
        if self.n_width <= width / self.width:
            return True
        return False

    def is_height_more_n_percent(self, contour: Contour):
        x, y, width, height = contour.bounding_rect
        if self.n_height <= height / self.height:
            return True
        return False


class RectangleMergingProcessor(Processor):

    def get_contours(self, contours: list, height=0, width=0):
        i = 0
        while i < len(contours) - 1:
            new_rect = self.get_merged_rectangles_if(contours[i], contours[i + 1])
            if new_rect:
                contours[i] = new_rect
                contours.pop(i + 1)
                i -= 1
            i += 1
        return contours
    
    def get_merged_rectangles_if(self, rect1: RectangleContour, rect2: RectangleContour) -> RectangleContour|None:
        return self.get_merged_rectangles(rect1, rect2)

    def get_merged_rectangles(self, rect1: RectangleContour, rect2: RectangleContour):
        x, y = min(rect1.x, rect2.x), min(rect1.y, rect2.y)
        width = max(rect1.x + rect1.width, rect2.x + rect2.width) - x
        height = max(rect1.y + rect1.height, rect2.y + rect2.height) - y
        return rect1.__class__(x, y, width, height)




class PositionProcessor(Processor):
    def __init__(self, hw_min, hw_max):
        self.hw_min = hw_min
        self.hw_max = hw_max
    
    def is_correct_contour(self, contour: Contour):
        x, y, width, height = contour.bounding_rect
        if self.hw_min <= height / width <= self.hw_max:
            return True
        return False



class RectangleSorterProcessor(Processor):
    
    def __init__(self, side_index: int=0) -> None:
        self.side_index = side_index

    def get_contours(self, contours: list, height=0, width=0):
        return sorted(contours, key=lambda contour: contour.bounding_rect[self.side_index])

