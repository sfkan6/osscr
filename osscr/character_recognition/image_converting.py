from abc import ABCMeta, abstractmethod
from cv2_detection.object_detection import Image
from ..sscr import CharImage


class ImageConverter:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def get_char_image(self, image: Image) -> CharImage:
        pass


class CV2ImageConverter(ImageConverter):
    
    def get_char_image(self, image: Image) -> CharImage:
        return CharImage(image._image.tolist())
