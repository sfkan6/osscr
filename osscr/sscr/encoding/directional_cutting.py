from abc import ABCMeta, abstractmethod
from .image_cutting import ImageCutter


class DirectionalLineCutter:
    __metaclass__ = ABCMeta

    def __init__(self, image_cutter):
        self.image_cutter = image_cutter

    def get_lines_by_locations(self, locations):
        return [self.get_line_by_location(location) for location in locations]

    @abstractmethod
    def get_line_by_location(self, location):
        pass

    @classmethod
    def create_by_image(cls, image):
        return cls(ImageCutter(image))


class HorizontalLineCutter(DirectionalLineCutter):
    def get_line_by_location(self, location):
        y = int(round(location * self.image_cutter.height))
        return self.image_cutter.get_horizontal_line_by_y(y)


class VerticalLineCutter(DirectionalLineCutter):
    def get_line_by_location(self, location):
        x = int(round(location * self.image_cutter.width))
        return self.image_cutter.get_vertical_line_by_x(x)
