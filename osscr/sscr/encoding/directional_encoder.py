from .sectional_encoding import SectionalEncoder
from .directional_cutting import (
    DirectionalLineCutter,
    HorizontalLineCutter,
    VerticalLineCutter,
)


class DirectionalEncoder:
    def __init__(
        self,
        sectional_encoder: SectionalEncoder,
        slice_locations: list,
        DirectionalCutter,
    ):
        self.sectional_encoder = sectional_encoder
        self.slice_locations = slice_locations
        self.DirectionalCutter = DirectionalCutter

    def set_threshold_number_of_pixels(self, threshold_number_of_pixels):
        self.sectional_encoder.set_threshold_number_of_pixels(
            threshold_number_of_pixels
        )

    def get_code_by_image(self, image):
        directional_cutter = self.DirectionalCutter.create_by_image(image)
        return self.get_code_by_directional_cutter(directional_cutter)

    def get_code_by_directional_cutter(self, directional_cutter: DirectionalLineCutter):
        slice_codes = []
        for locations in self.slice_locations:
            lines = directional_cutter.get_lines_by_locations(locations)
            slice_codes.append(
                self.sectional_encoder.get_conjunction_code_by_lines(lines)
            )
        return "".join(slice_codes)


class HorizontalEncoder(DirectionalEncoder):
    def __init__(self, sectional_encoder: SectionalEncoder, slice_locations: list):
        super().__init__(sectional_encoder, slice_locations, HorizontalLineCutter)


class VerticalEncoder(DirectionalEncoder):
    def __init__(self, sectional_encoder: SectionalEncoder, slice_locations: list):
        super().__init__(sectional_encoder, slice_locations, VerticalLineCutter)
