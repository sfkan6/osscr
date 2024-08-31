from ..image_detection import ImageDetector, CV2ThresholdImageDetector
from ..image_detection.cv2_detection import Thresher, Detector

from .character_threshing import CharacterHSVThresher
from .character_processing import CharacterRectangleProcessor



class CharacterThresholdImageDetector(CV2ThresholdImageDetector):
    def __init__(self):
        detector = Detector(CharacterHSVThresher(), CharacterRectangleProcessor())
        super().__init__(detector)


class CustomizableThresholdImageDetector(CV2ThresholdImageDetector):
    def __init__(self, thresher: Thresher):
        detector = Detector(thresher, CharacterRectangleProcessor())
        super().__init__(detector)

