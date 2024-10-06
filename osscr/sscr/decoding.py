class Decoder:
    codes = {}

    @classmethod
    def get_symbol_by_code(cls, code):
        code = "".join(code)
        return cls.codes.get(code, None)

    @classmethod
    def create_by_codes(cls, codes):
        cls.codes.update(codes)
        return cls()


class DigitDecoder(Decoder):
    codes = {
        "0101000": 1,
        "0110111": 2,
        "0101111": 3,
        "1101010": 4,
        "1001111": 5,
        "1011111": 6,
        "0101100": 7,
        "1111111": 8,
        "1101111": 9,
        "1111101": 0,
    }


class LetterDecoder(Decoder):
    codes = {
        "1111110": 'A',
        "1011011": 'b',
        "1010101": "C",
        "1011101": 'G',
        "0111011": 'd',
        "1010111": 'E',
        "1010110": "F",
        "1011010": 'h',
        "0001000": 'i',
        "0111001": 'J',
        "1010001": 'L',
    }


class CharacterDecoder(Decoder):
    codes = {**LetterDecoder.codes, **DigitDecoder.codes}
