from ..objects import Contour

class Processor:
    
    def __init__(self, height: int = 0, width: int = 0) -> None:
        self.set_height_and_width(height, width)
    
    def set_height_and_width(self, height: int, width: int) -> None:
        self.height = height
        self.width = width

    def get_contours(self, contours: list, height=0, width=0):
        self.set_height_and_width(height, width)
        return [contour for contour in contours if self.is_correct_contour(contour)]

    def is_correct_contour(self, contour: Contour):
        if contour:
            return True
        return False


class MultipleProcessor:
    def __init__(self, processors: list):
        self.processors = processors

    def get_contours(self, contours: list, height=0, width=0):
        for processor in self.processors:
            contours = processor.get_contours(contours, height, width)
        return contours

