from ..image_detection import ImageDetector, ThresholdImageDetector, Thresher, Detector, Image
from .threshing import CharacterHSVThresher
from .contour_processing import CharacterProcessor



class CharacterThresholdImageDetector(ThresholdImageDetector):
    def __init__(self):
        detector = Detector(CharacterHSVThresher(), CharacterProcessor())
        super().__init__(detector)


class CharacterThresholdImageDetectorWithThresher(ThresholdImageDetector):
    def __init__(self, thresher: Thresher):
        detector = Detector(thresher, CharacterProcessor())
        super().__init__(detector)

