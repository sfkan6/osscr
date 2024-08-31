from ..sscr import Recognizer, DigitRecognizer, SymbolRecognizer
from .character_image_detection import (
    ImageDetector, CV2ThresholdImageDetector, 
    CustomizableThresholdImageDetector, CharacterThresholdImageDetector,
)
from ..image_detection.cv2_detection import Image, Thresher, Detector


class UniversalCharacterRecognizer:
    def __init__(self, image_detector: ImageDetector, recognizer: Recognizer):
        self.image_detector = image_detector
        self.recognizer = recognizer

    def get_symbols(self, image: Image):
        images = self.image_detector.get_images(image)
        return [self.recognizer.get_symbol(image.image) for image in images]
 

class CharacterRecognizerConfigurableByThresher(UniversalCharacterRecognizer):
    def __init__(self, thresher: Thresher, recognizer: Recognizer):
        super().__init__(CustomizableThresholdImageDetector(thresher), recognizer)


class CustomizableCharacterRecognizer(UniversalCharacterRecognizer):
    def __init__(self, detector: Detector, recognizer: Recognizer):
        super().__init__(CV2ThresholdImageDetector(detector), recognizer)


class DisplayCharacterRecognizer(UniversalCharacterRecognizer):
    def __init__(self, recognizer: Recognizer):
        super().__init__(CharacterThresholdImageDetector(), recognizer)


class DisplayDigitRecognizer(DisplayCharacterRecognizer):
    def __init__(self):
        super().__init__(DigitRecognizer())


class DisplaySymbolRecognizer(DisplayCharacterRecognizer):
    def __init__(self, codes: dict={}):
        super().__init__(SymbolRecognizer.create_by_codes(codes))
