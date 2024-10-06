from cv2_detection.object_detection import Thresher, Detector, Image, Contour


class ImageDetector:
    def __init__(self, detector: Detector):
        self.detector = detector
    
    def get_images(self, image: Image) -> list[Image]:
        contours = self.detector.get_contours_by_image(image)
        return self.get_images_by_contours(image, contours)

    def get_images_by_contours(self, image: Image, contours: list[Contour]) -> list[Image]:
        return [image.get_image_by_bounding_rect(*contour.bounding_rect) for contour in contours]


class ThresholdImageDetector(ImageDetector):
    
    def get_images(self, image: Image) -> list[Image]:
        threshold_image = self.detector.thresher.get_finished_image(image)
        contours = self.detector.get_contours_by_image(image)
        return self.get_images_by_contours(threshold_image, contours)


