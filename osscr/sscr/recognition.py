from .decoding import Decoder, DigitDecoder, LetterDecoder, SymbolDecoder
from .encoding import UniversalEncoder, Encoder, DigitEncoder


class Recognizer:
    def __init__(self, encoder: UniversalEncoder, decoder: Decoder):
        self.encoder = encoder
        self.decoder = decoder
        self.code = ""

    def get_symbol(self, threshold_image):
        self.code = self.encoder.get_code_by_image(threshold_image)
        return self.decoder.get_symbol_by_code(self.code)


class DigitRecognizer(Recognizer):
    def __init__(self):
        super().__init__(DigitEncoder(), DigitDecoder())

class LetterRecognizer(Recognizer):
    def __init__(self):
        super().__init__(Encoder(), LetterDecoder())

class SymbolRecognizer(Recognizer):
    
    def __init__(self, decoder: Decoder):
        super().__init__(DigitEncoder(), decoder)

    @classmethod
    def create_by_default(cls):
        return cls(SymbolDecoder())

    @classmethod
    def create_by_codes(cls, codes: dict):
        return cls(SymbolDecoder.create_by_codes(codes))
