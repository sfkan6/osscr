from ..image_detection import ImageDetector, CV2ImageDetector
from ..image_detection.cv2_detection import Thresher, Detector

from .display_threshing import DisplayHSVThresher
from .display_processing import DisplayRectangleProcessor



class DisplayImageDetector(CV2ImageDetector):
    def __init__(self, hsv_ranges: list):
        detector = Detector(DisplayHSVThresher(hsv_ranges), DisplayRectangleProcessor())
        super().__init__(detector)


class CustomizableDisplayImageDetector(CV2ImageDetector):
    def __init__(self, thresher: Thresher):
        detector = Detector(thresher, DisplayRectangleProcessor())
        super().__init__(detector)

