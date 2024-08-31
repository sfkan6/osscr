from osscr.sscr import DigitRecognizer, SymbolRecognizer, Recognizer
from osscr.image_detection.cv2_detection import CV2Image, CV2Thresher, Image, Thresher
import os


class RecognizerTest:
    def __init__(self, recognizer: Recognizer) -> None:
        self.thresher = CV2Thresher()
        self.recognizer = recognizer

    def get_filename_and_value(self, dir_path):
        return [
            [filename, self.get_value_by_file(dir_path + filename)]
            for filename in os.listdir(dir_path)
        ]
    
    def get_value_by_file(self, file_path):
        image = CV2Image.read(file_path)
        threshold_image = self.thresher.get_threshold_image(image)
        return self.recognizer.get_symbol(threshold_image.image)


def test_digit():
    dir_path = "tests/digits/"
    recognizer_test = RecognizerTest(DigitRecognizer())

    filenames_and_values = recognizer_test.get_filename_and_value(dir_path)
    print(*filenames_and_values, sep="\n")


def test_symbol():
    dir_path = "tests/symbols/"
    codes = {'1101110': 'q', '1011101': 'G', '1010110': 'F', '1010101': 'C', '1111110': 'A'}
    recognizer_test = RecognizerTest(SymbolRecognizer.create_by_codes(codes))

    filenames_and_values = recognizer_test.get_filename_and_value(dir_path)
    print(*filenames_and_values, sep="\n")



if __name__ == '__main__':
    test_digit()
    test_symbol()
