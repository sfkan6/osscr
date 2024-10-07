from osscr import DisplaySymbolRecognizer, DisplayCharacterRecognizerWithThresher
from osscr.sscr import CharacterRecognizer
from cv2_detection import Image, HSVThresher
import os


class DisplaySymbolRecognizerTester:
    def __init__(self, display_symbol_recognizer: DisplaySymbolRecognizer) -> None:
        self.display_symbol_recognizer = display_symbol_recognizer

    def test(self, dir_path: str, image_name: str) -> list[str|list]:
        image = Image.read(dir_path + image_name)
        return [image_name, self.display_symbol_recognizer.get_symbols(image)]


class GlowingCharacterHSVThresher(HSVThresher):
    
    default_hsv_ranges = [[(0, 0, 210), (180, 240, 255)]]

    def __init__(self):
        super().__init__(self.default_hsv_ranges, open_iters=3, dilate_iters=1, close_iters=4)


class MyDisplaySymbolRecognizer(DisplayCharacterRecognizerWithThresher):
    def __init__(self):
        super().__init__(GlowingCharacterHSVThresher(), CharacterRecognizer.create_by_default())



def test(dir_path: str, image_name: str) -> None:
    recognizer = MyDisplaySymbolRecognizer()
    tester = DisplaySymbolRecognizerTester(recognizer)
    print(tester.test(dir_path, image_name))


def test_all(dir_path: str) -> None:
    recognizer = DisplaySymbolRecognizer()
    tester = DisplaySymbolRecognizerTester(recognizer)

    for filename in os.listdir(dir_path):
        print(tester.test(dir_path, filename))


def main():
    test_dir = 'test-images/'
    image_name= '9328.png'

    test(test_dir + 'displays/', image_name)
    test_all(test_dir + 'displays/')

if __name__ == '__main__':
    main()
