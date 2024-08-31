import numpy as np
from .sectional_encoding import SectionalEncoder
from .directional_encoder import DirectionalEncoder, HorizontalEncoder, VerticalEncoder


class UniversalEncoder:
    def __init__(self, *encoders: DirectionalEncoder):
        self.encoders = encoders

    def set_threshold_number_of_pixels(self, threshold_number_of_pixels):
        for encoder in self.encoders:
            encoder.set_threshold_number_of_pixels(threshold_number_of_pixels)

    def get_code_by_image(self, threshold_image):
        codes = [
            encoder.get_code_by_image(threshold_image) for encoder in self.encoders
        ]
        return "".join(codes)


class SevenSegmentEncoder(UniversalEncoder):
    def __init__(self, horizontal_slice_locations, vertical_slice_locations):
        horizontal_sectional_encoder = SectionalEncoder([1, 1], 1)
        vertical_sectional_encoder = SectionalEncoder([1, 2, 1], 1)
        horizontal_encoder = HorizontalEncoder(
            horizontal_sectional_encoder, horizontal_slice_locations
        )
        vertical_encoder = VerticalEncoder(
            vertical_sectional_encoder, vertical_slice_locations
        )
        super().__init__(horizontal_encoder, vertical_encoder)

    def get_code_by_image(self, threshold_image):
        self.set_threshold_number_of_pixels_by_height(threshold_image.shape[0])
        return super().get_code_by_image(threshold_image)

    def set_threshold_number_of_pixels_by_height(self, height):
        threshold_number_of_pixels = self.get_threshold_number_of_pixels_by_height(
            height
        )
        self.set_threshold_number_of_pixels(threshold_number_of_pixels)

    def get_threshold_number_of_pixels_by_height(self, height, part_of_height=0.04):
        return max(1, int(height * part_of_height))

   

class Encoder(SevenSegmentEncoder):

    def __init__(self):
        super().__init__([[0.25], [0.75]], [[0.4, 0.55]])

class DigitEncoder(Encoder):
    def get_code_by_image(self, threshold_image):
        if self.is_digit_one(threshold_image):
            threshold_image = self.get_extended_image_of_number_one(threshold_image)
        return super().get_code_by_image(threshold_image)

    def get_extended_image_of_number_one(self, threshold_image):
        height, width = threshold_image.shape
        extended_threshold_image = np.zeros((height, int(height * 2 / 3)), dtype=int)
        extended_threshold_image[-height:, -width:] = threshold_image
        return extended_threshold_image

    def is_digit_one(self, threshold_image):
        height, width = threshold_image.shape
        if height > width * 3:
            return True
        return False
