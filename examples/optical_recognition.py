from osscr import OpticalSymbolRecognizer, OpticalCharacterRecognizerWithThresher
from osscr import DisplaySymbolRecognizer, DisplayCharacterRecognizerWithDetector, DisplayCharacterRecognizerWithThresher 
from osscr.sscr import CharacterRecognizer
from cv2_detection import Image, HSVThresher, Thresher



class MyHSVThresher(HSVThresher):
    
    def __init__(self, hsv_ranges: list, open_iters=2, dilate_iters=5, close_iters=5):
        super().__init__(hsv_ranges, open_iters, dilate_iters, close_iters)


class GreenCharacterHSVThresher(HSVThresher):
    
    default_hsv_ranges = [[(0, 0, 170), (180, 255, 255)]]

    def __init__(self):
        super().__init__(self.default_hsv_ranges, open_iters=1, dilate_iters=1, close_iters=3)


class GlowingRedCharacterHSVThresher(HSVThresher):
    
    default_hsv_ranges = [[(0, 0, 210), (180, 245, 255)]]

    def __init__(self):
        super().__init__(self.default_hsv_ranges, open_iters=2, dilate_iters=1, close_iters=3)




def get_image_by_filename(filename: str) -> Image:
    file_path = "test-images/images/" + filename
    return Image.read(file_path)



def normal():
    filenames = ['4.png', '5.png', '6.png']
    image = get_image_by_filename(filenames[0])

    hsv_ranges = [[(0, 150, 80), (180, 255, 255)]]
    thresher = MyHSVThresher(hsv_ranges)
    
    recognizer = OpticalCharacterRecognizerWithThresher(thresher, DisplaySymbolRecognizer())
    print(recognizer.get_symbols(image))



def horizontal_separation():
    filenames = ['1.png', '2.png']
    image = get_image_by_filename(filenames[1])

    # hsv_ranges = [[(0, 100, 30), (10, 255, 255)], [(175, 0, 40), (180, 255, 255)]] # True red hsv
    hsv_ranges = [[(0, 150, 80), (180, 255, 255)]]
    thresher = MyHSVThresher(hsv_ranges)
    
    first_part = image.get_image_by_bounding_rect(0, 0, image.width // 2, image.height // 2)
    second_part = image.get_image_by_bounding_rect(image.width // 2, 0, image.width, image.height)
    
    display_recognizer_for_first = DisplayCharacterRecognizerWithThresher(GlowingRedCharacterHSVThresher(), CharacterRecognizer.create_by_default())
    first_recognizer = OpticalCharacterRecognizerWithThresher(thresher, display_recognizer_for_first)
    print(first_recognizer.get_symbols(first_part))

    second_recognizer = OpticalCharacterRecognizerWithThresher(thresher, DisplaySymbolRecognizer())
    print(second_recognizer.get_symbols(second_part))


def vertical_separation():
    filenames = ['3.png']
    image = get_image_by_filename(filenames[0])

    display_recognizer = DisplayCharacterRecognizerWithThresher(GreenCharacterHSVThresher(), CharacterRecognizer.create_by_default())

    hsv_ranges = [((30, 150, 4), (70, 255, 255))] # True green hsv
    thresher = MyHSVThresher(hsv_ranges)
    
    recognizer = OpticalCharacterRecognizerWithThresher(thresher, display_recognizer)
    print(recognizer.get_symbols(image))



def main():
    normal()
    horizontal_separation()
    vertical_separation()



if __name__ == '__main__':
    main()
