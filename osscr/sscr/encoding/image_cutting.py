import numpy as np


class ImageCutter:
    def __init__(self, image):
        self._image = np.array(image)

    @property
    def image(self):
        return self._image.copy()

    @property
    def width(self):
        return self.image.shape[1]

    @property
    def height(self):
        return self.image.shape[0]

    def get_horizontal_line_by_y(self, y):
        return self.get_image_by_coordinates(0, y, -1, y + 1)[0]

    def get_vertical_line_by_x(self, x):
        image_line = self.get_image_by_coordinates(x, 0, x + 1, -1)
        return np.concatenate(image_line)

    def get_image_by_coordinates(self, x0, y0, x1, y1):
        return self.image[y0:y1, x0:x1]
