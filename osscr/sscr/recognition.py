from .decoding import Decoder, DigitDecoder, LetterDecoder, CharacterDecoder
from .encoding import CharImage, Encoder, DefaultEncoder


class Recognizer:
    def __init__(self, encoder: Encoder, decoder: Decoder) -> None:
        self.encoder = encoder
        self.decoder = decoder
        self.code = ""

    def get_char_by_image(self, image: CharImage) -> str|int:
        self.code = self.encoder.get_code_by_image(image)
        return self.decoder.get_symbol_by_code(self.code)


class DefaultRecognizer(Recognizer):
    def __init__(self, decoder: Decoder) -> None:
        super().__init__(DefaultEncoder(), decoder)

class LetterRecognizer(DefaultRecognizer):
    def __init__(self) -> None:
        super().__init__(LetterDecoder())

class DigitRecognizer(DefaultRecognizer):
    def __init__(self) -> None:
        super().__init__(DigitDecoder())
    
    def get_char_by_image(self, image: CharImage) -> str | int:
        if self.is_digit_one(image):
            return 1
        return super().get_char_by_image(image)

    def is_digit_one(self, image: CharImage) -> bool:
        height, width = image.height, image.width
        if height > width * 3:
            return True
        return False

class CharacterRecognizer(DigitRecognizer):
     
    def __init__(self, decoder: Decoder) -> None:
        super().__init__()
        self.decoder = decoder

    @classmethod
    def create_by_default(cls):
        return cls(CharacterDecoder())

    @classmethod
    def create_by_codes(cls, codes: dict):
        return cls(CharacterDecoder.create_by_codes(codes))
