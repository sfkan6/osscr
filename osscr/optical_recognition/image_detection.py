from ..image_detection import ImageDetector, Thresher, Detector, Image
from .threshing import DisplayHSVThresher
from .contour_processing import DisplayRectangleProcessor



class DisplayImageDetector(ImageDetector):
    def __init__(self, hsv_ranges: list):
        detector = Detector(DisplayHSVThresher(hsv_ranges), DisplayRectangleProcessor())
        super().__init__(detector)


class DisplayImageDetectorWithThresher(ImageDetector):
    def __init__(self, thresher: Thresher):
        detector = Detector(thresher, DisplayRectangleProcessor())
        super().__init__(detector)

