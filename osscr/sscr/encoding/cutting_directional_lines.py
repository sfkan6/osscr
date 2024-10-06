from abc import ABCMeta, abstractmethod
from .char_image import CharImage


class DirectionalLineCutter:
    __metaclass__ = ABCMeta

    def __init__(self, image: CharImage) -> None:
        self.set_image(image)
    
    def set_image(self, image: CharImage) -> None:
        self._image = image

    def get_lines_by_locations(self, locations: list[float]) -> list[list]:
        return [self.get_line_by_location(location) for location in locations]

    @abstractmethod
    def get_line_by_location(self, location: float) -> list:
        pass


class HorizontalLineCutter(DirectionalLineCutter):
    
    def get_line_by_location(self, location: float) -> list:
        y = int(round(location * self._image.height))
        return self._image.get_horizontal_line(y)

class VerticalLineCutter(DirectionalLineCutter):
    
    def get_line_by_location(self, location: float) -> list:
        x = int(round(location * self._image.width))
        return self._image.get_vertical_line(x)
