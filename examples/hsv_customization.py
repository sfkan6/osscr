from osscr import DisplaySymbolRecognizer, CharacterRecognizerConfigurableByThresher
from osscr.sscr import SymbolRecognizer
from osscr.image_detection.cv2_detection import CV2Image, CV2HSVThresher


class MyHSVThresher(CV2HSVThresher):

    def __init__(self, hsv_ranges: list, open_iters=1, dilate_iters=3, close_iters=2):
        super().__init__(hsv_ranges, open_iters, dilate_iters, close_iters)



def main():
    image = CV2Image.read("tests/displays/75EG.png")

    hsv_ranges = [[(0, 0, 210), (180, 255, 255)]]
    thresher = MyHSVThresher(hsv_ranges)

    # threshold_image = thresher.get_finished_image(image)
    # threshold_image.write("test.png")

    recognizer = CharacterRecognizerConfigurableByThresher(thresher, SymbolRecognizer.create_by_default())
    print(recognizer.get_symbols(image))


if __name__ == '__main__':
    main()
