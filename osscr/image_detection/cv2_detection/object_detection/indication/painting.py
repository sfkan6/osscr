from ..objects import Image, Contour
from abc import abstractmethod


class Painter:
    def __init__(self, color=(0, 255, 0), thickness=3):
        self.color = color
        self.thickness = thickness

    @abstractmethod
    def rectangle(self, image: Image, contour: Contour) -> Image:
        pass

    @abstractmethod
    def point(self, image: Image, contour: Contour) -> Image:
        pass

    @abstractmethod
    def contour(self, image: Image, contour: Contour) -> Image:
        pass
