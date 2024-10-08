from cv2_detection import HSVThresher


class CharacterHSVThresher(HSVThresher):
    
    default_hsv_ranges = [[(0, 0, 210), (180, 255, 255)]]

    def __init__(self):
        super().__init__(self.default_hsv_ranges, open_iters=1, dilate_iters=2, close_iters=3)


