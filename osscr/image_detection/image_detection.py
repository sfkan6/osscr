from .image_cutting import ImageCutter, CV2ImageCutter
from .cv2_detection import Detector, Image


class ImageDetector:
    def __init__(self, image_cutter: ImageCutter, detector: Detector):
        self.image_cutter = image_cutter
        self.detector = detector
    
    def get_images(self, image: Image) -> list[Image]:
        rectangle_contours = self.detector.get_contours_by_image(image)
        return self._get_images_by_contours(image, rectangle_contours)
    
    def _get_images_by_contours(self, image: Image, contours: list) -> list[Image]:
        self.image_cutter.set_image(image)
        return self.image_cutter.get_images_by_contours(contours)



class CV2ImageDetector(ImageDetector):
    def __init__(self, detector: Detector):
        image_cutter = CV2ImageCutter(Image([]))
        super().__init__(image_cutter, detector)


class CV2ThresholdImageDetector(CV2ImageDetector):
    
    def get_images(self, image: Image) -> list[Image]:
        threshold_image = self.detector.thresher.get_finished_image(image)
        rectangle_contours = self.detector.get_contours_by_image(image)
        return self._get_images_by_contours(threshold_image, rectangle_contours)


