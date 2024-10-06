from cv2_detection import HSVThresher


class DisplayHSVThresher(HSVThresher):
    
    def __init__(self, hsv_ranges: list):
        super().__init__(hsv_ranges, open_iters=1, dilate_iters=5, close_iters=5)

