from .image_threshing import Thresher
from .contour_processing import MultipleProcessor
from ..objects import Image, Contour, EmptyContour


class Detector:

    def __init__(self, thresher: Thresher, multiple_processor: MultipleProcessor):
        self.thresher = thresher
        self.multiple_processor = multiple_processor

    def get_best_contour_by_image(self, image: Image) -> Contour:
        contours = self.get_contours_by_image(image)
        if len(contours) == 0:
            return EmptyContour()
        return contours[0]

    def get_contours_by_image(self, image: Image) -> list:
        contours = self.thresher.get_contours(image)
        return self.multiple_processor.get_contours(contours, image.height, image.width)
