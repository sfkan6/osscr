from ..sscr import Recognizer, DigitRecognizer, CharacterRecognizer
from .image_converting import ImageConverter, CV2ImageConverter
from .image_detection import (
    ImageDetector, ThresholdImageDetector, 
    CharacterThresholdImageDetectorWithThresher, CharacterThresholdImageDetector,
    Thresher, Detector, Image
)


class UniversalDisplayCharacterRecognizer:
    def __init__(self, image_detector: ImageDetector, image_converter: ImageConverter, recognizer: Recognizer):
        self.image_detector = image_detector
        self.recognizer = recognizer
        self.image_converter = image_converter

    def get_symbols(self, image: Image) -> list[str|int]:
        images = self.image_detector.get_images(image)
        return [self._get_char_by_image(image) for image in images]

    def _get_char_by_image(self, image: Image) -> str|int:
        char_image = self.image_converter.get_char_image(image)
        return self.recognizer.get_char_by_image(char_image)


class DisplayCharacterRecognizer(UniversalDisplayCharacterRecognizer):
    def __init__(self, image_detector: ImageDetector, recognizer: Recognizer):
        super().__init__(image_detector, CV2ImageConverter(), recognizer)


class DisplayCharacterRecognizerWithDetector(DisplayCharacterRecognizer):
    def __init__(self, detector: Detector, recognizer: Recognizer):
        super().__init__(ThresholdImageDetector(detector), recognizer)

class DisplayCharacterRecognizerWithThresher(DisplayCharacterRecognizer):
    def __init__(self, thresher: Thresher, recognizer: Recognizer):
        super().__init__(CharacterThresholdImageDetectorWithThresher(thresher), recognizer)


class ConfiguredDisplayCharacterRecognizer(DisplayCharacterRecognizer):
    def __init__(self, recognizer: Recognizer):
        super().__init__(CharacterThresholdImageDetector(), recognizer)

class DisplayDigitRecognizer(ConfiguredDisplayCharacterRecognizer):
    def __init__(self):
        super().__init__(DigitRecognizer())

class DisplaySymbolRecognizer(ConfiguredDisplayCharacterRecognizer):
    def __init__(self, codes: dict={}):
        super().__init__(CharacterRecognizer.create_by_codes(codes))
