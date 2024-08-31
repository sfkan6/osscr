from ..detection import Detector
from ..objects import Image
from .painting import Painter


class Indicator:
   
    def __init__(self, detector: Detector, painter: Painter):
        self.detector = detector
        self.painter = painter

    def display_as_rectangle(self, image: Image):
        return self.painter.rectangle(image.copy(), self._get_contour(image))

    def display_as_point(self, image: Image):
        return self.painter.point(image.copy(), self._get_contour(image))

    def display_as_contour(self, image: Image):
        return self.painter.contour(image.copy(), self._get_contour(image))

    def _get_contour(self, image: Image):
        return self.detector.get_best_contour_by_image(image)



class MultipleIndicator:

    def __init__(self, indicators):
        self.indicators = indicators

    def display_all_as_rectangles(self, image: Image):
        for indicator in self.indicators:
            image = indicator.display_as_rectangle(image)
        return image

    def display_all_as_points(self, image: Image):
        for indicator in self.indicators:
            image = indicator.display_as_point(image)
        return image

    def display_all_as_contours(self, image: Image):
        for indicator in self.indicators:
            image = indicator.display_as_contour(image)
        return image
