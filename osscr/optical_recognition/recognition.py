from ..character_recognition import DisplayCharacterRecognizer, DisplayDigitRecognizer, DisplaySymbolRecognizer
from .image_detection import ImageDetector, DisplayImageDetector, DisplayImageDetectorWithThresher, Thresher, Detector, Image


class OpticalCharacterRecognizer:

    def __init__(
        self, image_detector: ImageDetector, character_recognizer: DisplayCharacterRecognizer
    ) -> None:
        self.image_detector = image_detector
        self.character_recognizer = character_recognizer

    def get_symbols(self, image: Image) -> list[list[str|int]]:
        images = self.image_detector.get_images(image)
        return [self.character_recognizer.get_symbols(image) for image in images]


class OpticalCharacterRecognizerWithDetector(OpticalCharacterRecognizer):
    def __init__(self, detector: Detector, character_recognizer: DisplayCharacterRecognizer):
        super().__init__(ImageDetector(detector), character_recognizer)

class OpticalCharacterRecognizerWithThresher(OpticalCharacterRecognizer):
    def __init__(self, thresher: Thresher, character_recognizer: DisplayCharacterRecognizer) -> None:
        super().__init__(DisplayImageDetectorWithThresher(thresher), character_recognizer)


class OpticalRecognizer(OpticalCharacterRecognizer):
    def __init__(self, hsv_ranges: list, character_recognizer: DisplayCharacterRecognizer):
        super().__init__(DisplayImageDetector(hsv_ranges), character_recognizer)

class OpticalDigitRecognizer(OpticalRecognizer):
    def __init__(self, hsv_ranges):
        super().__init__(hsv_ranges, DisplayDigitRecognizer())

class OpticalSymbolRecognizer(OpticalRecognizer):
    def __init__(self, hsv_ranges, codes={}):
        super().__init__(hsv_ranges, DisplaySymbolRecognizer(codes))
