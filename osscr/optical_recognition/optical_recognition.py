from ..character_recognition import UniversalCharacterRecognizer, DisplayDigitRecognizer, DisplaySymbolRecognizer
from .display_image_detection import ImageDetector, CV2ImageDetector, DisplayImageDetector, CustomizableDisplayImageDetector
from ..image_detection.cv2_detection import Image, Thresher, Detector, CV2Painter


class UniversalOpticalRecognizer:

    def __init__(
        self, image_detector: ImageDetector, character_recognizer: UniversalCharacterRecognizer
    ):
        self.image_detector = image_detector
        self.character_recognizer = character_recognizer

    def get_symbols(self, image: Image):
        images = self.image_detector.get_images(image)[:]
        return [self.character_recognizer.get_symbols(image) for image in images]


class OpticalRecognizerConfigurableByThresher(UniversalOpticalRecognizer):
    def __init__(self, thresher: Thresher, character_recognizer: UniversalCharacterRecognizer):
        super().__init__(CustomizableDisplayImageDetector(thresher), character_recognizer)


class CustomizableOpticalRecognizer(UniversalOpticalRecognizer):
    def __init__(self, detector: Detector, character_recognizer: UniversalCharacterRecognizer):
        super().__init__(CV2ImageDetector(detector), character_recognizer)


class OpticalRecognizer(UniversalOpticalRecognizer):
    def __init__(self, hsv_ranges: list, character_recognizer: UniversalCharacterRecognizer):
        super().__init__(DisplayImageDetector(hsv_ranges), character_recognizer)


class OpticalDigitRecognizer(OpticalRecognizer):
    def __init__(self, hsv_ranges):
        super().__init__(hsv_ranges, DisplayDigitRecognizer())


class OpticalSymbolRecognizer(OpticalRecognizer):
    def __init__(self, hsv_ranges, codes={}):
        super().__init__(hsv_ranges, DisplaySymbolRecognizer(codes))
