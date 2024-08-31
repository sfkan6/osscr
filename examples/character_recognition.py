from osscr import DisplaySymbolRecognizer, CharacterRecognizerConfigurableByThresher
from osscr.sscr import SymbolRecognizer
from osscr.image_detection.cv2_detection import CV2Image, CV2HSVThresher
import os


class GlowingCharacterHSVThresher(CV2HSVThresher):
    
    default_hsv_ranges = [[(0, 0, 210), (180, 240, 255)]]

    def __init__(self):
        super().__init__(self.default_hsv_ranges, open_iters=3, dilate_iters=1, close_iters=4)


class MyDisplaySymbolRecognizer(CharacterRecognizerConfigurableByThresher):
    def __init__(self):
        super().__init__(GlowingCharacterHSVThresher(), SymbolRecognizer.create_by_default())


def test():
    glowing_image_name = "9328.png"
    dir_path = "tests/displays/"
    recognizer = MyDisplaySymbolRecognizer()

    image = CV2Image.read(dir_path + glowing_image_name)
    print([glowing_image_name, recognizer.get_symbols(image)])


def test_all():
    dir_path = "tests/displays/"
    recognizer = DisplaySymbolRecognizer()

    for filename in os.listdir(dir_path):
        image = CV2Image.read(dir_path + filename)
        print([filename, recognizer.get_symbols(image)])


def main():
    test()
    test_all()

if __name__ == '__main__':
    main()
