from .cv2_detection import Contour


class RectangleContour(Contour):
    
    def __init__(self, x, y, width, height) -> None:
        self.set_bounding_rect(x, y, width, height)
    
    @property
    def area(self) -> int | float:
        return self.width * self.height

    @property
    def bounding_rect(self) -> list:
        return [self.x, self.y, self.width, self.height]

    def get_points(self):
        return (self.x, self.y), (self.x + self.width, self.y + self.height)

    def set_bounding_rect(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @classmethod
    def create_by_contour(cls, contour: Contour):
        return cls(*contour.bounding_rect)

    def __repr__(self) -> str:
        return self.__str__()

    def __str__(self) -> str:
        return f"{self.bounding_rect}"

