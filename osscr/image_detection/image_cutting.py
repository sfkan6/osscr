from .cv2_detection import Image, CV2Image, Contour
from abc import abstractmethod


class ImageCutter:

    def __init__(self, image: Image) -> None:
        self.set_image(image)
    
    def set_image(self, image: Image):
        self._image = image

    @abstractmethod
    def get_images_by_contours(self, contours: list) -> list:
        return [self.get_image_by_contour(contour) for contour in contours]
   
    @abstractmethod
    def get_image_by_contour(self, contour: Contour) -> Image:
        pass


class CV2ImageCutter(ImageCutter):

    @property
    def image(self):
        return self._image.copy()
    
    def get_image_by_contour(self, contour: Contour) -> Image:
        x, y, width, height = contour.bounding_rect
        return self._get_image_by_coordinates(x, y, x + width, y + height)

    def _get_image_by_coordinates(self, x0, y0, x1, y1):
        return CV2Image(self._image.image[y0:y1, x0:x1])
