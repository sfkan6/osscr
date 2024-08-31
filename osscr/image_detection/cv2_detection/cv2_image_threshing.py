from .object_detection import Image, Thresher
from .cv2_objects import CV2Image, CV2Contour
import cv2, numpy as np


class CV2Thresher(Thresher):

    def __init__(self, open_iters=1, dilate_iters=2, close_iters=2):
        self.open_iters = open_iters
        self.dilate_iters = dilate_iters
        self.close_iters = close_iters

    def get_threshold_image(self, image: Image) -> Image:
        gray_image = cv2.cvtColor(image.image, cv2.COLOR_BGR2GRAY)
        _, threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)
        return CV2Image(threshold_image)

    def get_enhanced_threshold_image(self, threshold_image: Image) -> Image:
        image = threshold_image.image
        kernel = np.ones((3, 3), np.uint8)
        image = cv2.morphologyEx(
            image, cv2.MORPH_OPEN, kernel, iterations=self.open_iters
        )
        image = cv2.morphologyEx(
            image, cv2.MORPH_DILATE, kernel, iterations=self.dilate_iters
        )
        image = cv2.morphologyEx(
            image, cv2.MORPH_CLOSE, kernel, iterations=self.close_iters
        )
        return CV2Image(image)

    def get_contours_by_threshold_image(self, threshold_image: Image) -> list:
        contours, _ = cv2.findContours(
            threshold_image.image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        return [CV2Contour(Contour) for Contour in contours]


class CV2HSVThresher(CV2Thresher):
   
    def __init__(self, hsv_ranges: list, open_iters=3, dilate_iters=4, close_iters=3):
        self.hsv_ranges = hsv_ranges
        super().__init__(open_iters, dilate_iters, close_iters)

    def get_threshold_image(self, image: Image) -> Image:
        gray_image = cv2.cvtColor(image.image, cv2.COLOR_BGR2HSV)
        mask = np.zeros((image.height, image.width), np.uint8)
        for hsv_range in self.hsv_ranges:
            mask += cv2.inRange(gray_image.copy(), *hsv_range)
        return CV2Image(mask)

    def get_enhanced_threshold_image(self, threshold_image: Image) -> Image:
        image = threshold_image.image
        kernel = np.ones((3, 3), np.uint8)
        image = cv2.morphologyEx(
            image, cv2.MORPH_OPEN, kernel, iterations=self.open_iters
        )
        image = cv2.morphologyEx(
            image, cv2.MORPH_DILATE, kernel, iterations=self.dilate_iters
        )
        image = cv2.morphologyEx(
            image, cv2.MORPH_CLOSE, kernel, iterations=self.close_iters
        )
        return CV2Image(image)

