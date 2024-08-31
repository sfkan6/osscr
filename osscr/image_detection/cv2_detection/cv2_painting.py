from .object_detection import Image, Contour
from .object_detection.indication import Painter
from .cv2_objects import CV2Image
import cv2


class CV2Painter(Painter):

    def rectangle(self, image: Image, contour: Contour) -> Image:
        x, y, w, h = contour.bounding_rect
        new_image = image.image
        cv2.rectangle(new_image, (x, y), (x + w, y + h), color=self.color, thickness=self.thickness)
        return CV2Image(new_image)

    def point(self, image: Image, contour: Contour) -> Image:
        x, y, w, h = contour.bounding_rect
        new_image = image.image
        cv2.circle(new_image, (x + w // 2, y + h // 2), radius=0, color=self.color, thickness=self.thickness)
        return CV2Image(new_image)

    def contour(self, image: Image, contour: Contour) -> Image:
        new_image = image.image
        cv2.drawContours(new_image, [contour.contour], 0, color=self.color, thickness=self.thickness)
        return CV2Image(new_image)
