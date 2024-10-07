from osscr import DisplayCharacterRecognizerWithThresher
from osscr.sscr import CharacterRecognizer
from cv2_detection import Image, HSVThresher



class MyHSVThresher(HSVThresher):

    def __init__(self, hsv_ranges: list, open_iters=1, dilate_iters=3, close_iters=2):
        super().__init__(hsv_ranges, open_iters, dilate_iters, close_iters)



def main():
    image_path = 'test-images/displays/75EG.png'
    image = Image.read(image_path)
    
    # Configurable parameters
    hsv_ranges = [[(0, 0, 210), (180, 255, 255)]]
    options = {
        'open_iters': 1, 
        'dilate_iters': 3, 
        'close_iters': 2,
    }

    thresher = MyHSVThresher(hsv_ranges, **options)
    # threshold_image = thresher.get_finished_image(image)
    # threshold_image.write("test.png")

    recognizer = DisplayCharacterRecognizerWithThresher(thresher, CharacterRecognizer.create_by_default())
    print(recognizer.get_symbols(image))


if __name__ == '__main__':
    main()
