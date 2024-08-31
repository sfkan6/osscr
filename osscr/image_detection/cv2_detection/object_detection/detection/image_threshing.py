from abc import abstractmethod
from ..objects import Image


class Thresher:
    
    def get_contours(self, image: Image) -> list:
        threshold_image = self.get_finished_image(image)
        return self.get_contours_by_threshold_image(threshold_image)

    def get_finished_image(self, image: Image) -> Image:
        threshold_image = self.get_threshold_image(image)
        return self.get_enhanced_threshold_image(threshold_image)
    
    @abstractmethod
    def get_threshold_image(self, image: Image) -> Image:
        pass

    @abstractmethod
    def get_enhanced_threshold_image(self, threshold_image: Image) -> Image:
        pass
 
    @abstractmethod
    def get_contours_by_threshold_image(self, threshold_image: Image) -> list:
        pass


class HSVThresher(Thresher):
    pass 
