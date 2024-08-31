from __future__ import annotations
from abc import abstractmethod


class Contour:
    def __init__(self, contour) -> None:
        self.contour = contour

    @property
    @abstractmethod
    def area(self) -> int|float:
        pass

    @property
    @abstractmethod
    def bounding_rect(self) -> list:
        pass


class EmptyContour(Contour):
    def __init__(self) -> None:
        super().__init__([])

    @property
    def area(self) -> int | float:
        return 0

    @property
    def bounding_rect(self) -> list:
        return [0, 0, 0, 0]


class Image:
    def __init__(self, image) -> None:
        self.image = image

    @property
    @abstractmethod
    def height(self) -> int:
        pass

    @property
    @abstractmethod
    def width(self) -> int:
        pass

    @property
    @abstractmethod
    def shape(self) -> list:
        pass

    @abstractmethod
    def copy(self) -> Image:
        return Image([])

    @abstractmethod
    def write(self, path) -> None:
        pass

    @classmethod
    @abstractmethod
    def read(cls, path) -> Image:
        pass



class Camera:

    @property
    @abstractmethod
    def is_connected(self) -> bool:
        pass

    @abstractmethod
    def get_image(self) -> Image:
        pass

    @abstractmethod
    def frame_to_bytes(self, image: Image) -> bytes:
        pass

