from osscr.sscr import Recognizer, DigitRecognizer, CharacterRecognizer, CharImage
from cv2_detection import Image, Thresher
import os



class RecognizerTester:
    def __init__(self, recognizer: Recognizer) -> None:
        self.thresher = Thresher()
        self.recognizer = recognizer

    def get_filename_and_value(self, dir_path: str) -> list[list[str|int]]:
        return [
            [filename, self.get_value_by_file(dir_path + filename)]
            for filename in os.listdir(dir_path)
        ]
    
    def get_value_by_file(self, file_path: str) -> str|int:
        image = Image.read(file_path)
        threshold_image = self.thresher.get_threshold_image(image)
        char_image = CharImage(threshold_image._image.tolist())
        return self.recognizer.get_char_by_image(char_image)



def test_digit(dir_path: str) -> None:
    recognizer_tester = RecognizerTester(DigitRecognizer())
    filenames_and_values = recognizer_tester.get_filename_and_value(dir_path)
    print(*filenames_and_values, sep="\n")


def test_symbol(dir_path: str, codes: dict={}) -> None:
    recognizer_tester = RecognizerTester(CharacterRecognizer.create_by_codes(codes))
    filenames_and_values = recognizer_tester.get_filename_and_value(dir_path)
    print(*filenames_and_values, sep="\n")



def main():
    codes = {
        '1101110': 'q', 
        '1011101': 'G', 
        '1010110': 'F', 
        '1010101': 'C', 
        '1111110': 'A'
    }
    test_dir = 'test-images/'
    test_digit(test_dir + 'digits/')
    test_symbol(test_dir + 'symbols/', codes)


if __name__ == '__main__':
    main()
