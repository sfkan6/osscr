from .sectional_encoding import SectionalEncoder
from .cutting_directional_lines import DirectionalLineCutter, HorizontalLineCutter, VerticalLineCutter
from .char_image import CharImage


class DirectionalEncoder:
    def __init__(self, sectional_encoder: SectionalEncoder, line_cutter: DirectionalLineCutter, list_of_locations: list[list[float]]) -> None:
        self.sectional_encoder = sectional_encoder
        self.list_of_locations = list_of_locations
        self.line_cutter = line_cutter

    def set_number_of_thresholds(self, number_of_thresholds: int) -> None:
        self.sectional_encoder.set_number_of_thresholds(number_of_thresholds)

    def get_code_by_image(self, image: CharImage) -> str:
        self.line_cutter.__init__(image)
        return self._get_code()

    def _get_code(self) -> str:
        slice_codes = []
        for locations in self.list_of_locations:
            lines = self.line_cutter.get_lines_by_locations(locations)
            slice_codes.append(self.sectional_encoder.get_conjunction_code_by_lines(lines))
        return "".join(slice_codes)


class HorizontalEncoder(DirectionalEncoder):
    def __init__(self, sectional_encoder: SectionalEncoder, list_of_locations: list[list[float]]) -> None:
        super().__init__(sectional_encoder, HorizontalLineCutter(CharImage([])), list_of_locations)


class VerticalEncoder(DirectionalEncoder):
    def __init__(self, sectional_encoder: SectionalEncoder, list_of_locations: list[list[float]]) -> None:
        super().__init__(sectional_encoder, VerticalLineCutter(CharImage([])), list_of_locations)
