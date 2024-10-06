

class CharImage:
    def __init__(self, image: list[list[int|float]]) -> None:
        self._image = image
    
    @property
    def width(self) -> int:
        return len(self._image[0])
 
    @property
    def height(self) -> int:
        return len(self._image)

    def get_horizontal_line(self, y) -> list[int|float]:
        y = min(abs(y), self.height)
        return self._image[y]

    def get_vertical_line(self, x) -> list[int|float]:
        x = min(abs(x), self.width)
        return [line[x] for line in self._image]



